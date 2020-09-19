import os
import sys
from configparser import ConfigParser
from UIconfig import adbTool

import xlwt
from xlutils.copy import copy
import xlrd
from azure.devops.connection import Connection
from bs4 import BeautifulSoup
from msrest.authentication import BasicAuthentication
from azure.devops.v6_0.work_item_tracking import WorkItemTrackingClient
from azure.devops.v6_0.work_item_tracking.models import JsonPatchOperation


class CreateBug:

    def __init__(self):
        """
        init class
        Fill in with your personal access token and org URL
        """
        self.personal_access_token = 'ldjpzf2w67hno5f3zsphgg2f2y2wg4m56icsfkrjs5f72mmowkgq'
        self.organization_url = 'https://dev.azure.com/saic-iov'

    def read_html(self, htmlpath):
        """
        读取Html文件返回BeautifulSoup对象
        :param htmlpath:
        :return:
        """
        with open(htmlpath, 'r', encoding='utf-8') as htmlfile:
            htmlhandle = htmlfile.read()
            soup = BeautifulSoup(htmlhandle, 'lxml')
        return soup

    def saveBuglist(self, data):
        """
        保存bug列表
        :param data: bug信息
        :param data: bug信息   type:workItem类型
        :return: 无返回值
        """
        project_name = data.fields['Custom.ProjectName']
        filename = 'Report/buglist/' + project_name + '_BugList.xlsx'
        workbook = xlrd.open_workbook(filename)
        sheet = workbook.sheet_by_index(0)
        rowNum = sheet.nrows
        colNum = sheet.ncols
        newbook = copy(workbook)
        newsheet = newbook.get_sheet(0)
        # 在末尾增加新行
        newsheet.write(rowNum, 0, data.fields['System.Id'])
        newsheet.write(rowNum, 1, project_name)
        newsheet.write(rowNum, 2, str(data.fields['Microsoft.VSTS.TCM.SystemInfo']).split('：')[1])
        newsheet.write(rowNum, 3, data.fields['Custom.AVN_Moudle'])
        newsheet.write(rowNum, 4, data.fields['System.Title'])
        newsheet.write(rowNum, 5, data.fields['System.CreatedDate'])
        newsheet.write(rowNum, 6, data.fields['System.CreatedBy']['uniqueName'])
        newsheet.write(rowNum, 7, data.fields['Microsoft.VSTS.Common.Priority'])
        newsheet.write(rowNum, 8, data.fields['Microsoft.VSTS.Common.Severity'])
        # newsheet.write(rowNum, 9, data.fields['前置条件'])
        newsheet.write(rowNum, 10, data.fields['Microsoft.VSTS.TCM.ReproSteps'])
        # newsheet.write(rowNum, 11, data.fields['ExpectedResult期望结果'])
        # newsheet.write(rowNum, 12, data.fields['ActuralResult实际结果'])
        # 覆盖保存
        newbook.save(filename)

    def read_Value(self, module, key):
        """
        根据key读取配置文件中的value值
        :param module:  配置文件中的模块名
        :param key:   配置文件中的key值
        :return: 返回key对应value值
        """
        cfg = ConfigParser()
        cfg.read('./Mconfig/Module_Owner.ini')
        return cfg.get(module, key)

    def create_Attachment(self, WorkItemParm, path):
        # 压缩log文件
        path = adbTool.adbtool().zip_file_path(path)
        upload_stream = open(path, mode='rb')
        attachment = WorkItemParm.create_attachment(upload_stream, project='SOIMT-AUTOTEST-BUG',
                                                    file_name=path.split('/')[-1],
                                                    upload_type='Simple', area_path='SOIMT-AUTOTEST-BUG')
        return attachment.url

    def getBugInfo(self, id, expand='ALL'):
        """
        根据bugid 获取bug的详细信息
        :param id: bugID
        :param expand:   默认获取改bug的所有信息，包括link、附件
        :return:  Returns a single work item.
        """
        # Create a connection to the org
        credentials = BasicAuthentication('', self.personal_access_token)
        connection = Connection(base_url=self.organization_url, creds=credentials)

        # Get a client (the "core" client provides access to projects, teams, etc)
        core_client = connection.clients.get_core_client()

        # Get the first page of projects
        get_projects_response = core_client.get_projects()
        while get_projects_response is not None:
            if get_projects_response.continuation_token is not None and get_projects_response.continuation_token != "":
                # Get the next page of projects
                get_projects_response = core_client.get_projects(
                    continuation_token=get_projects_response.continuation_token)
            else:
                # All projects have been retrieved
                get_projects_response = None

        WorkItemParm = WorkItemTrackingClient(base_url=self.organization_url, creds=credentials)
        bug = WorkItemParm.get_work_item(id=int(id), expand=expand)
        return bug

    def creatBug(self, project_name, version, title, module, owner, error, logPath):
        """
        Create Devops Bug
        :return: return bugDetail
        """
        # Create a connection to the org
        credentials = BasicAuthentication('', self.personal_access_token)
        connection = Connection(base_url=self.organization_url, creds=credentials)

        # Get a client (the "core" client provides access to projects, teams, etc)
        core_client = connection.clients.get_core_client()

        # Get the first page of projects
        get_projects_response = core_client.get_projects()
        while get_projects_response is not None:
            if get_projects_response.continuation_token is not None and get_projects_response.continuation_token != "":
                # Get the next page of projects
                get_projects_response = core_client.get_projects(
                    continuation_token=get_projects_response.continuation_token)
            else:
                # All projects have been retrieved
                get_projects_response = None

        # 连接客户端
        WorkItemParm = WorkItemTrackingClient(base_url=self.organization_url, creds=credentials)
        # 创建attachment url
        attachment_url = self.create_Attachment(WorkItemParm, logPath)
        # 准备bug的Json数据
        bugJson = [
            JsonPatchOperation(
                op='add',
                path='/fields/System.TeamProject',
                value='SOIMT-AUTOTEST-BUG'
            ),
            JsonPatchOperation(
                op='add',
                path='/fields/System.IterationPath',
                value='SOIMT-AUTOTEST-BUG'
            ),

            JsonPatchOperation(
                op='add',
                path='/fields/System.AreaPath',
                value='SOIMT-AUTOTEST-BUG'
            ),
            JsonPatchOperation(
                op='add',
                path='/fields/System.Title',
                value=title
            ),
            JsonPatchOperation(
                op='add',
                path='/fields/System.AssignedTo',
                value=owner
            ),
            JsonPatchOperation(
                op='add',
                path='/fields/Microsoft.VSTS.Common.Priority',
                value='2'
            ),
            JsonPatchOperation(
                op='add',
                path='/fields/Microsoft.VSTS.Common.Severity',
                value='2 - High'
            ),
            JsonPatchOperation(
                op='add',
                path='/fields/Custom.Compoonent',
                value='AVN'
            ),
            JsonPatchOperation(
                op='add',
                path='/fields/Custom.ProjectName',
                value=project_name
            ),
            JsonPatchOperation(
                op='add',
                path='/fields/Custom.AVN_Moudle',
                value=module
            ),
            JsonPatchOperation(
                op='add',
                path='/fields/Custom.Stage',
                value='ALL'
            ),
            JsonPatchOperation(
                op='add',
                path='/fields/Custom.AVNVersion',
                # value=version
                value='default'
            ),
            JsonPatchOperation(
                op='add',
                path='/fields/操作步骤',
                value='100%'
            ),
            JsonPatchOperation(
                op='add',
                path='/fields/前置条件',
                value='adb模式打开'
            ),
            JsonPatchOperation(
                op='add',
                path='/fields/ExpectedResult期望结果',
                value='正常运行 monkey，无异常报出 '
            ),
            JsonPatchOperation(
                op='add',
                path='/fields/ActuralResult实际结果',
                value='运行过程中发生异常。报错信息如下：  <br>' + error
            ),

            JsonPatchOperation(
                op='add',
                path='/fields/Custom.TboxVersion',
                value='Default'
            ),
            JsonPatchOperation(
                op='add',
                path='/fields/Microsoft.VSTS.TCM.SystemInfo',
                value='版本号：' + version
            ),
            JsonPatchOperation(
                op='add',
                path='/fields/Microsoft.VSTS.TCM.ReproSteps',
                value='1，打开adb模式；<br>'
                      '2，执行monkey指令: <br> adb shell monkey -p 包名 -v -v -v -s 500 --ignore-crashes --ignore-timeouts'
                      ' --ignore-security-exceptions --kill-process-after-error --pct-trackball 0 --pct-nav 0 '
                      '--pct-syskeys 0  --pct-anyevent 0 --pct-flip 0  --throttle 500 7200'
            ),
            JsonPatchOperation(
                op='add',
                path="/relations/-",
                value={
                    "rel": "AttachedFile",
                    "url": attachment_url,
                    "attributes": {
                        "comment": ""
                    }
                }
            ),
        ]
        print(module)
        bug = WorkItemParm.create_work_item(bugJson, 'SOIMT-AUTOTEST-BUG', 'Bug')
        return bug

    def get_BugInfo(self, html):
        buglist = []
        try:
            soup = self.read_html(html)
        except FileNotFoundError:
            print(html + '文件不存在。')
            os._exit(0)
        message = soup.find('body')
        title = message.find_all(attrs={'class': 'attribute'})
        project = title[0].text.split(':')[1].strip(" ")
        AvnVersion = title[1].text.split(':  ')[1].strip(" ")
        tester = title[2].text.split(":")[1].strip(" ")
        message = message.find_all('pre')
        for detail in message:
            errorInfo = {}
            try:
                failCase = detail.text.strip()
                if failCase.startswith('f') and (
                        failCase.__contains__('***CRASH***') or
                        failCase.__contains__('***ANR***') or
                        failCase.__contains__('***Exception***')):
                    failDetail = failCase.split('\n')
                    packageName = failDetail[2].split(" ")[0].split("=")[1]
                    ProjectName = self.read_Value('Project', project)
                    module = self.read_Value('Package', packageName)
                    Owner = self.read_Value('Owner', module)
                    title = '[SOIMT][AutoTest][' + ProjectName + '][monkey][' + module + ']应用执行monkey命令时发生异常'
                    error = failDetail[10]
                    logPath = str(failDetail[3]).split(':')[1].split('***********')[0]
                    errorInfo['project'] = ProjectName
                    errorInfo['version'] = ProjectName + ":SOC_" + AvnVersion
                    errorInfo['AVN_Module'] = module
                    errorInfo['title'] = title
                    errorInfo['AssignedTo'] = Owner
                    errorInfo['error'] = error
                    errorInfo['logPath'] = logPath
                    buglist.append(errorInfo)
                else:
                    pass
            except Exception as e:
                print('getValueError:' + str(e))
                continue
        return buglist

    def readBugExcle(self, project):
        AllInfo = []
        if not os.path.isdir('Report/buglist/'):
            os.makedirs('Report/buglist/')
        if not os.path.isfile('Report/buglist/' + project + '_BugList.xlsx'):
            print('buglist文件不存在，将重新创建。')
            # 无文件时创建
            wbk = xlwt.Workbook()
            newsheet = wbk.add_sheet('BugList', cell_overwrite_ok=True)
            head = ['bugID', 'ProjectName', 'Version', 'Moudle', 'Title', 'CreatedDate', 'CreatedBy', 'Priority',
                    'Severity', '前置条件', 'TestSteps', 'ExpectedResult期望结果', 'ActuralResult实际结果']
            for index, value in enumerate(head):
                newsheet.write(0, index, value)
            wbk.save('Report/buglist/' + project + '_BugList.xlsx')
            return AllInfo
        excle = xlrd.open_workbook('Report/buglist/' + project + '_BugList.xlsx')
        sheet = excle.sheet_by_index(0)
        rows = sheet.nrows
        for row in range(rows):
            AllBug = []
            project = sheet.cell_value(row, 1)
            AvnVersion = sheet.cell_value(row, 2)
            AVN_Module = sheet.cell_value(row, 3)
            AllBug.append(project)
            AllBug.append(AvnVersion)
            AllBug.append(AVN_Module)
            AllInfo.append(AllBug)
        return AllInfo

    def CreateBug(self, filePath):
        Allerror = self.get_BugInfo(filePath)
        buglist = []
        for item in Allerror:
            itmes = []
            project_name = item['project']
            version = item['version']
            title = item['title']
            module = item['AVN_Module']
            owner = item['AssignedTo']
            error = item['error']
            logPath = item['logPath']
            itmes.append(project_name)
            itmes.append(version)
            itmes.append(module)
            if itmes in self.readBugExcle(project_name):
                continue
            else:
                itmes.append(logPath)
                try:
                    buginfo = self.creatBug(project_name, version, title, module, owner, error, logPath)
                    buglist.append(buginfo)
                except Exception as e:
                    print(e)
                    pass
        if len(buglist) == 0:
            print('无新增bug需要创建。')
        for i in buglist:
            self.saveBuglist(self.getBugInfo(i.id))


if __name__ == "__main__":
    files = sys.argv[1]
    Bug = CreateBug()
    if str(files).__contains__(','):
        fileList = str(files).split(",")
        for item in fileList:
            print('开始依据' + item + '创建bug.....')
            Bug.CreateBug(item)
            print(item + '，bug创建完成。')
    else:
        print('开始依据' + files + '创建bug.....')
        Bug.CreateBug(files)
        print(files + '，bug创建完成。')
