#coding=utf-8
import unittest
from selenium import webdriver
from pages.Base_CommodityClass import AddCommdityClass
from pages.login import LoginSuccess
import time

class TestAddCommClass(unittest.TestCase):
    '''基础商品分类'''
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.acc=AddCommdityClass(cls.driver)
        lo=LoginSuccess(cls.driver)
        lo.login(keep_login=True)#login中默认值给的false，当传入ture时执行click_keep_login（7天自动登录）

    def test_commcalss(self):
        '''添加电商商品分类'''
        cs= "自动添加分类" + time.strftime("%Y_%m_%d_%H_%M_%S")
        self.acc.addcommclass(cs)
        result = self.acc.is_addcommclass_sucess(cs)
        print(result)
        self.assertTrue(result)

    @classmethod
    def tearDownClass(cls) -> None:
         cls.driver.quit()

if __name__ == '__main__':
    unittest.main()


