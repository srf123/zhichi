#conding:utf-8
import unittest
from selenium import webdriver
from pages.login import LoginSuccess
from pages.Appoint_CommodityManage import CommodityManage
import time
class CommodifyManage(unittest.TestCase):
    '''行业预约商品管理'''
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver=webdriver.Chrome()
        lg=LoginSuccess(cls.driver)
        lg.login()
        cls.cm=CommodityManage(cls.driver)
    def test_add_commdifysucess(self):
        '''成功添加行业预约商品'''
        stime=time.strftime("%Y_%m_%d_%H_%M_%S")
        commname="行业预约商品"+stime
        self.cm.add_commodity(commname)
        result=self.cm.is_addCommodifySucess(commname)
        self.assertTrue(result)
    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()

