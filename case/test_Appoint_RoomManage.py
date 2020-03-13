#coding=utf-8
import unittest
from selenium import webdriver
from pages.login import LoginSuccess
from pages.Appoint_Roommanage import RoomManage
import time
class RoomManage(unittest.TestCase):
    """行业预约库存/房间管理"""
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        log = LoginSuccess(cls.driver)
        log.login()
        cls.rm = RoomManage(cls.driver)

    def test_rommmanage(self):
        '''成功添加行业预约库存/房间'''
        stime=time.strftime("%Y_%m_%d_%H_%M_%S")
        roomname="标准间"+stime
        self.rm.roommanage(roomname)
        result = self.rm.is_addroomsucess(roomname)
        #print(result)
        self.assertTrue(result)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()





