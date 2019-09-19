#coding=utf-8
import  unittest
from selenium import webdriver
from pages.addCommodity import Commodity
from pages.login import LoginSuccess
import time


class Test_add_Commodity(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.commo  = Commodity(cls.driver)
        lo = LoginSuccess(cls.driver)
        lo.login(keep_login = True)

    def test_add_commodity(self):
        com = "自动添加商品" + time.strftime("%Y_%m_%d_%H_%M_%S")
        self.commo.add_commodity(com)
        result = self.commo.is_addComm_successful(com)
        print(result)
        self.assertTrue(result)

    # @classmethod
    # def tearDownClass(cls) -> None:
    #    cls.driver.quit()

if __name__ == '__main__':
     unittest.main()
