#coding:uft-8
import unittest
from selenium import webdriver
from pages.Appoint_ReservatSpecificat import Reseevatspceificat
from pages.login import LoginSuccess
import time
class ReservatSpecificat(unittest.TestCase):
    '''行业预约规格设置'''
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome()
        log=LoginSuccess(cls.driver)
        log.login()
        cls.rs = Reseevatspceificat(cls.driver)
    def test_reservatSpecificat(self):
        '''成功添加行业预约三级规格'''
        stime=time.strftime("%Y_%m_%d_%H_%M_%S")
        one='南山'+stime
        self.rs.reservatSpecificat(stime)
        #一级规格添加后判断
        resultone=self.rs.is_Reservatspecificat(one)
        print(resultone)
        self.assertTrue(resultone)
        #二级规格添加后判断
        two='标准间'+stime
        resulttwo=self.rs.is_ReservatSpecificatTwo(two)
        self.assertTrue(resulttwo)


    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()

