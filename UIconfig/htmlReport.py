# -*- coding=utf-8 -*-
import datetime
import sys
import time, os
from shutil import copyfile

from UIconfig import XmlMaker


class Template_mixin(object):
    STATUS = {
        0: '通过',
        1: '失败',
        2: '错误',
    }

    DEFAULT_TITLE = '车机自动化测试报告'
    DEFAULT_DESCRIPTION = ''
    DEFAULT_TESTER = 'Tester'
    DEFAULT_PROJECT = 'Demo'
    DEFAULT_VERSION = ""

    """html报告"""
    HTML_TMPL = r"""
        <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
        <html lang="en" xmlns="http://www.w3.org/1999/xhtml">
        <head>
            <meta charset="UTF-8">
            <title>自动化测试报告</title>
            <link href="http://libs.baidu.com/bootstrap/3.0.3/css/bootstrap.min.css" rel="stylesheet">
            <h2 style="font-family: Microsoft YaHei">%(title)s</h2>
            <p class='attribute'><strong>项目名称 : </strong> %(project)s</p>
            <p class='attribute'><strong>测试版本 : </strong> %(version)s</p>
            <p class='attribute'><strong>测试人员 : </strong> %(tester)s</p>
            <p class='attribute'><strong>开始时间 : </strong> %(start)s</p>
            <p class='attribute'><strong>合计耗时 : </strong> %(total)s</p>
            <p class='attribute'><strong>测试结果 : </strong> %(result)s</p>
            <style type="text/css" media="screen">
        body  { font-family: Microsoft YaHei,Tahoma,arial,helvetica,sans-serif;padding: 20px;}
        </style>
        </head>
        %(stylesheet)s
        %(report_tmpl)s
        %(html_body)s
        %(ending)s
<script language="javascript" type="text/javascript">
output_list = Array();
// 修改按钮颜色显示错误问题 --Findyou v0.8.2.3

$("button[id^='true']").addClass("btn btn-success");
$("button[id^='false']").addClass("btn btn-danger");
$("button[id^='error']").addClass("btn btn-warning");

/*level
增加分类并调整，增加error按钮事件 --Findyou v0.8.2.3
0:Pass    //pt none, ft hiddenRow, et hiddenRow
1:Failed  //pt hiddenRow, ft none, et hiddenRow
2:Error    //pt hiddenRow, ft hiddenRow, et none
3:All     //pt none, ft none, et none
4:Summary //all hiddenRow
*/

//add Error button event --Findyou v0.8.2.3
function showCase(level) {
    trs = document.getElementsByTagName("tr");
    for (var i = 0; i < trs.length; i++) {
        tr = trs[i];
        id = tr.id;
        if (id.substr(0,2) == 'ft') {
            if (level == 0 || level == 2 || level == 4 ) {
                tr.className = 'hiddenRow';
            }
            else {
                tr.className = '';
            }
        }
        if (id.substr(0,2) == 'pt') {
            if (level == 1 || level == 2 || level == 4) {
                tr.className = 'hiddenRow';
            }
            else {
                tr.className = '';
            }
        }
        if (id.substr(0,2) == 'et') {
            if (level == 0 || level == 1 || level == 4) {
                tr.className = 'hiddenRow';
            }
            else {
                tr.className = '';
            }
        }
    }
        """
    STYLESHEET_TMPL = """
    <style type="text/css" media="screen">
    body        { font-family: Microsoft YaHei,Tahoma,arial,helvetica,sans-serif;padding: 20px; font-size: 100%; }
    table       { font-size: 100%; }

    /* -- heading ---------------------------------------------------------------------- */
    .heading {
        margin-top: 0ex;
        margin-bottom: 1ex;
    }

    .heading .description {
        margin-top: 4ex;
        margin-bottom: 6ex;
    }

    /* -- report ------------------------------------------------------------------------ */
    #total_row  { font-weight: bold; }
    .passCase   { color: #5cb85c; }
    .failCase   { color: #d9534f; font-weight: bold; }
    .errorCase  { color: #f0ad4e; font-weight: bold; }
    .hiddenRow  { display: none; }
    .testcase   { margin-left: 2em; }
    </style>
    """

    REPORT_TMPL = r"""
    <p id='show_detail_line'>
    <a class="btn btn-primary" href='javascript:showCase(4)'>概要{ %(passrate)s }</a>
    <a class="btn btn-success" href='javascript:showCase(0)'>通过{ %(Pass)s }</a>
    <a class="btn btn-danger" href='javascript:showCase(1)'>失败{ %(fail)s }</a>
    <a class="btn btn-warning" href='javascript:showCase(2)'>错误{ %(error)s }</a>
    <a class="btn btn-info" href='javascript:showCase(3)'>所有{ %(count)s }</a>
    </p>"""

    HTML_BODY = r"""<body>
            <!-- 执行模块 -->
            <table id='result_table' class="table table-condensed table-bordered table-hover">
                <colgroup>
                   <col align='left' />
                   <col align='right' />
                   <col align='right' />
                   <col align='right' />
                   <col align='right' />
                </colgroup>
                <tr id='header_row' class="text-center success" style="font-weight: bold;font-size: 14px;">
                    <th colspan="2" class="text-center success">功能模块</th>
                    <th colspan="2" class="text-center success">用例编号</th>
                   <!-- <th class="text-center success">总计</th> -->
                   <!-- <th class="text-center success">通过</th> -->
                    <th colspan="3" class="text-center success">描述</th>
                    <th colspan="2" class="text-center success">断言值</th>
                    <th colspan="3" class="text-center success">详细</th>
                    <th colspan="2" class="text-center success">截图</th>
                </tr>
                %(table_tr2)s

            </table>
        </body>
        </html>"""
    # 总数据
    TABLE_TMPL_TOTAL = """
        <tr class='failClass warning'>
            <td >%(version)s</td>
            <td>%(radio)s</td>
            <td>%(runstarttime)s</td>
            <td>%(runstoptime)s</td>
        </tr>"""
    # 详情表头
    TABLE_TMPL_MODULE = """
        <tr id='header_row' class="text-center success" style="font-weight: bold;font-size: 14px;">
            <th class="text-center success">%(module)s</th>
            <th class="text-center success">%(caseID)s</th>
            <th class="text-center success">%(casetotal)s</th>
            <th class="text-center success">%(passtotal)s</th>
            <th class="text-center success">%(failtotal)s</th>
            <th class="text-center success">%(errortotal)s</th>
            <th class="text-center success">%(detail)s</th>
            <th class="text-center success">%(pic)s</th>
        </tr>"""
    # case数据
    TABLE_TMPL_CASE = """
        <tr class=%(caseType)s style="font-weight: bold;font-size: 12px;">
            <th colspan="2" class="text-center success">%(module)s</th>
            <th colspan="2" class="text-center success">%(caseID)s</th>
            <th colspan="3" class="text-center success">%(description)s</th>
            <th colspan="2" class="text-center success">%(caseAssert)s</th>
            <th colspan="3" class="text-center success">%(result)s<br />%(detail)s</th>  
            <th colspan="2" class="text-center success">
            <a href=%(dir)s>%(pic)s</a>
            </th>
        </tr>"""

    ENDING = """
    <div id='ending'>&nbsp;</div>
    <div style=" position:fixed;right:50px; bottom:30px; width:20px; height:20px;cursor:pointer">
    <a href="#"><span class="glyphicon glyphicon-eject" style = "font-size:30px;" aria-hidden="true">
    </span></a></div>
    """

    def __init__(self, stream=sys.stdout, verbosity=1, title=None, description=None, tester=None, startTime=None,
                 project=None, version=None):
        self.stream = stream
        self.verbosity = verbosity
        if title is None:
            self.title = self.DEFAULT_TITLE
        else:
            self.title = title
        if description is None:
            self.description = self.DEFAULT_DESCRIPTION
        else:
            self.description = description
        if tester is None:
            self.tester = self.DEFAULT_TESTER
        else:
            self.tester = tester
        if project is None:
            self.project = self.DEFAULT_PROJECT
        else:
            self.project = project
        if version is None:
            self.version = self.DEFAULT_VERSION
        else:
            self.version = version
        self.startTime = startTime
        self.longtime = datetime.datetime.now() - self.startTime

    def writeHtml(self, caseList):

        table_tr1 = ""
        numfail = 0
        numsucc = 0
        numerr = 0
        # caseModule = ''
        # ModuleP = 0
        # ModuleF = 0
        # ModuleE = 0
        # 数据部分
        # print(caseList)
        for case in caseList:
            Module = case['module']
            # print(Module)
            # print(caseModule)
            # if caseModule != Module:
            #     caseModule = Module
            #     # 详情数据
            #     table_td_module = self.TABLE_TMPL_MODULE % dict(module=caseModule, caseID="",
            #                                                     casetotal=ModuleP + ModuleF + ModuleE,
            #                                                     passtotal=ModuleP, failtotal=ModuleF,
            #                                                     errortotal=ModuleE,
            #                                                     detail="Pass" if ModuleE + ModuleF == 0 else "Fail",
            #                                                     pic='')
            #     table_tr1 += table_td_module
            #
            #     ModuleP = 0
            #     ModuleF = 0
            #     ModuleE = 0
            caseID = case['caseID']
            caseDescription = case['description']
            caseAssert = case['assert']
            caseDetail = case['detail']
            caseResult = case['result']
            pic = case['pic']
            if caseResult.lower() == 'true':
                pic = ""
                # ModuleP = ModuleP + 1
                numsucc = numsucc + 1
            elif caseResult.lower() == 'false':
                # ModuleF = ModuleF + 1
                numfail = numfail + 1
            elif caseResult.lower() == 'error':
                # ModuleE = ModuleE + 1
                numerr = numerr + 1
            else:
                pass
            # case数据
            table_td_case = self.TABLE_TMPL_CASE % dict(caseType=caseResult, module=Module, caseID=caseID,
                                                        description=caseDescription,
                                                        result=caseResult, detail=caseDetail, caseAssert=caseAssert,
                                                        dir='../screen/' + pic,
                                                        pic=pic)
            table_tr1 += table_td_case
        try:
            passrate = '{:.2f}%'.format(numsucc / len(caseList) * 100)
        except:
            passrate = '0.00%'

        # 表头总数
        total_str = '共 %s，通过 %s，失败 %s，错误 %s，通过率 %s' % (len(caseList), numsucc, numfail, numerr, passrate)
        print(total_str)
        stylesheet = self.STYLESHEET_TMPL

        tmpl = self.REPORT_TMPL % dict(passrate=passrate, Pass=numsucc, fail=numfail, error=numerr,
                                       count=numerr + numfail + numsucc)

        body = self.HTML_BODY % dict(table_tr2=table_tr1)

        output = self.HTML_TMPL % dict(title=self.title, project=self.project, tester=self.tester, start=self.startTime,
                                       total=self.longtime, version=self.version,
                                       result=total_str, stylesheet=stylesheet, report_tmpl=tmpl, html_body=body,
                                       ending=self.ENDING)
        # 生成html报告
        filename = 'report_ui_{date}.html'.format(date=time.strftime('%Y%m%d%H%M%S'))
        dir = os.path.abspath('.') + '/Report/'
        if not os.path.exists(dir):
            os.makedirs(dir)
        filename = os.path.join(dir, filename)

        with open(filename, 'wb') as f:
            f.write(output.encode('utf-8'))
        try:
            copyfile(filename, dir + 'report.html')
        except:
            print("Unexpected error:", sys.exc_info())
        read = XmlMaker.XmlMaker()
        read.makexml(caseList, str(numsucc), str(numfail), str(numerr), str(self.startTime), str(self.longtime))
