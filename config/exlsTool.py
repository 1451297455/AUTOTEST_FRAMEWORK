import xlrd


class exlsTool():

    def __init__(self):
        self.caseFile = xlrd.open_workbook("./TestCase/Case.xlsx")
        self.allSheet = self.caseFile.sheet_names()
        self.suitList = {}
        self.testSuit = self.caseFile.sheet_by_name("suit")
        self.row = self.testSuit.nrows
        for i in range(1, self.row):
            key = self.testSuit.cell_value(i, 0)
            value = self.testSuit.cell_value(i, 1)
            self.suitList[key] = value

    def getSuit(self):
        self.suitList = {}
        self.testSuit = self.caseFile.sheet_by_name("suit")
        row = self.testSuit.nrows
        for i in range(1, row):
            key = self.testSuit.cell_value(i, 0)
            value = self.testSuit.cell_value(i, 1)
            self.suitList[key] = value
        return self.suitList

    def getCaseCell(self, sheetName, row, col):
        if sheetName not in self.allSheet:
            return "sheetName not exist"
        self.testCase = self.caseFile.sheet_by_name(sheetName)
        rowCount = self.testCase.nrows
        if row >= rowCount:
            return "error"
        else:
            return self.testCase.cell_value(row, col)

    def getCaseId(self, sheetName, row):
        if sheetName not in self.allSheet:
            return "sheetName not exist"
        self.testCase = self.caseFile.sheet_by_name(sheetName)
        rowCount = self.testCase.nrows
        if row >= rowCount:
            return "error"
        else:
            return str(self.testCase.cell_value(row, 0))

    def getCaseDescription(self, sheetName, row):
        if sheetName not in self.allSheet:
            return "sheetName not exist"
        self.testCase = self.caseFile.sheet_by_name(sheetName)
        rowCount = self.testCase.nrows
        if row >= rowCount:
            return "error"
        else:
            return str(self.testCase.cell_value(row, 2))

    def getClass(self, sheetName, row):
        if sheetName not in self.allSheet:
            return "sheetName not exist"
        self.testCase = self.caseFile.sheet_by_name(sheetName)
        rowCount = self.testCase.nrows
        if row >= rowCount:
            return "error"
        elif str(self.testCase.cell_value(row, 3)).__contains__("::"):
            return str.split(self.testCase.cell_value(row, 3), "::", 2)[0]
        else:
            try:
                return str.split(self.testCase.cell_value(row, 3), "/", 2)[0]
            except:
                return "empty"

    def getMethod(self, sheetName, row):
        if sheetName not in self.allSheet:
            return "sheetName not exist"
        self.testCase = self.caseFile.sheet_by_name(sheetName)
        rowCount = self.testCase.nrows
        if row >= rowCount:
            return "error"
        elif str(self.testCase.cell_value(row, 3)).__contains__("::"):
            return str.split(self.testCase.cell_value(row, 3), "::", 2)[1]
        else:
            try:
                return str.split(self.testCase.cell_value(row, 3), "/", 2)[1]
            except:
                return "empty"

    def getParam(self, sheetName, row):
        if sheetName not in self.allSheet:
            return "sheetName not exist"
        self.testCase = self.caseFile.sheet_by_name(sheetName)
        rowCount = self.testCase.nrows
        if row >= rowCount:
            para = []
        else:
            para = str.split(self.testCase.cell_value(row, 4), "/", 9)
        return para[0: -1]

    def getAssert(self, sheetName, row):
        if sheetName not in self.allSheet:
            return "sheetName not exist"
        self.testCase = self.caseFile.sheet_by_name(sheetName)
        rowCount = self.testCase.nrows
        if row >= rowCount:
            return "error"
        else:
            return str(self.testCase.cell_value(row, 5))

    def getCheckValue(self, sheetName, row):
        if sheetName not in self.allSheet:
            return "sheetName not exist"
        self.testCase = self.caseFile.sheet_by_name(sheetName)
        rowCount = self.testCase.nrows
        if row >= rowCount:
            return "error"
        else:
            return str(self.testCase.cell_value(row, 6))

    def getValuation(self, sheetName, row):
        if sheetName not in self.allSheet:
            return "sheetName not exist"
        self.testCase = self.caseFile.sheet_by_name(sheetName)
        rowCount = self.testCase.nrows
        if row >= rowCount:
            return "error"
        else:
            return str(self.testCase.cell_value(row, 7))

    def getResult(self, className, MethodName, Param):
        if className == "" or MethodName == "":
            return False
        try:
            package = __import__("page", fromlist=[className])
            pyName = getattr(package, className)
            '''
            如果模块导入成功，该模块下的所有py文件会作为模块的属性，因此使用getattr(模块，文件名)获取即可
                    文件名不需要加.py后缀
            '''
        except AttributeError:
            package = __import__("page", fromlist=[className])
            pyName = getattr(package, className)
        '''
        如果模块导入成功，该模块下的所有py文件会作为模块的属性，因此使用getattr(模块，文件名)获取即可
                文件名不需要加.py后缀
        '''
        # 根据子类名称从fileName.py中获取该类
        NameClass = getattr(pyName, className)
        # 实例化对象
        classa = NameClass()
        # 调用返回方法函数
        runMethod = getattr(classa, MethodName)
        argCount = runMethod.__code__.co_argcount
        ParamCount = len(Param)
        ##self is also a parameter no need to input
        if argCount - 1 == ParamCount:
            res = runMethod(*Param)
            print(res)
            return res
        else:
            return False
