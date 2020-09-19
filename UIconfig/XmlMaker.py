from xml.dom.minidom import Document


class XmlMaker:

    def makexml(self, caseList, numsucc, numfail, numerr, startTime, longtime):
        doc = Document()
        orderpack = doc.createElement("testsuites")
        orderpack.setAttribute('error', numerr)
        orderpack.setAttribute('failure', numfail)
        orderpack.setAttribute('name', '')
        orderpack.setAttribute('pass', numsucc)
        orderpack.setAttribute('tests', str(len(caseList)))
        orderpack.setAttribute('time', longtime)
        orderpack.setAttribute('timestamp', startTime)
        doc.appendChild(orderpack)
        perTime = float(longtime.split(":")[-1]) / len(caseList)
        failnum = 0
        passnum = 0
        erronum = 0
        testsuit = []
        objectTemp = None

        for i in caseList:
            module = i['module']
            caseID = i['caseID']
            detail = i['detail']
            result = i['result']

            if module not in testsuit:
                failnum = 0
                passnum = 0
                erronum = 0

                testsuit.append(module)

                objectE = doc.createElement('testsuite')
                objectE.setAttribute("name", module)

                objectTemp = objectE
            else:
                objectE = objectTemp

            if result == 'True':
                passnum = passnum + 1
            elif result == 'False':
                failnum = failnum + 1
            else:
                erronum = erronum + 1

            objectTemp.setAttribute("error", str(erronum))
            objectTemp.setAttribute("fail", str(failnum))
            objectTemp.setAttribute("pass", str(passnum))
            objectTemp.setAttribute("tests", str(erronum + failnum + passnum))
            objectTemp.setAttribute("time", '11.231312')

            objectcontent = doc.createElement("testcase")
            objectcontent.setAttribute('classname', module + "_" + caseID)
            objectcontent.setAttribute('name', caseID)
            objectcontent.setAttribute('status', result)
            objectcontent.setAttribute('time', str(perTime))
            if result == 'False':
                objectFail = doc.createElement('failure')
                objectFail.setAttribute('message', detail)
                objectFail.setAttribute('type', 'ErrorType')
                objectcontent.appendChild(objectFail)
            objectE.appendChild(objectcontent)

            if len(testsuit) == 1:
                orderpack.setAttribute('name', testsuit[0] + ' Model TestReport')
            elif len(testsuit) > 1:
                orderpack.setAttribute('name', 'Multi Model TestReport')

            orderpack.appendChild(objectE)

        f = open('./Report/AVNTestReport.xml', 'w+')
        doc.writexml(f, indent='\t', newl='\n', addindent='\t', encoding='utf-8')
        f.close()
