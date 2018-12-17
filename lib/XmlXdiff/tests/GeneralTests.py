import unittest
import inspect
from XmlXdiff import getPath, XDiffer
from XmlXdiff.XReport import DrawXmlDiff


class CompareAll(unittest.TestCase):

    @staticmethod
    def execute_old(folder_name):
        _i = XDiffer.XDiffExecutor()
        _i.path1 = "{}\\tests\\{}\\a.xml".format(getPath(), folder_name)
        _i.path2 = "{}\\tests\\{}\\b.xml".format(getPath(), folder_name)
        _i.run()

    @staticmethod
    def execute(folder_name):
        _path1 = "{}\\tests\\{}\\a.xml".format(getPath(), folder_name)
        _path2 = "{}\\tests\\{}\\b.xml".format(getPath(), folder_name)
        _i = DrawXmlDiff(_path1, _path2)
        _i.save()

    def test1(self):
        name = inspect.currentframe().f_code.co_name
        self.__class__.execute(name)

    def test2(self):
        name = inspect.currentframe().f_code.co_name
        self.__class__.execute(name)

    def test3(self):
        name = inspect.currentframe().f_code.co_name
        self.__class__.execute(name)

    def test4(self):
        name = inspect.currentframe().f_code.co_name
        self.__class__.execute(name)

    def test5(self):
        name = inspect.currentframe().f_code.co_name
        self.__class__.execute(name)

    def test6(self):
        name = inspect.currentframe().f_code.co_name
        self.__class__.execute(name)

    def test7(self):
        name = inspect.currentframe().f_code.co_name
        self.__class__.execute(name)

    def test8(self):
        name = inspect.currentframe().f_code.co_name
        self.__class__.execute(name)
