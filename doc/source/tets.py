import os
import sys
from os.path import abspath, dirname

# sys.path.append(os.path.abspath('..'))
print(os.path.abspath('../../page'))
print(sys.path)
print(sys.path.insert(0,os.path.abspath('../../page')))
print(sys.path)
# print(dirname(dirname(dirname(abspath(__file__)))))
# print(abspath(__file__))
# print(sys.path)


class rse:
    """
    dasdasdasda
    """

    def test(self):
        """
        returm1
        :return:
        """
        return 'a'
