#coding=utf-8
import unittest
from selenium import webdriver
from pages.login import LoginSuccess
from pages.addFreightTemplate import AddFreightTemplate
import time

class AddFreightTemplate(unittest.TestCase):
    '''添加运费模板'''
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver=webdriver.Chrome()
        cls.aft=AddFreightTemplate(cls.driver)
        ls=LoginSuccess(cls.driver)
        ls.login()


    def test_addFreightTemplate(self):
        '''成功添加运费模板'''
        nam = "运费模板" + time.strftime("%Y_%m_%d_%H_%M_%S")
        self.aft.addfreighttemplate(nam)
        result = self.aft.is_addFreightTempSuccess(nam)
        print(result)
        self.assertTrue(result)


    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
if __name__ == '__main__':
    unittest.main()