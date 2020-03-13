#coding:utf-8
import unittest
from selenium import webdriver
from pages.UserManage import UserManage_
from pages.login import LoginSuccess


class UserManage(unittest.TestCase):
    '''用户管理'''
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        lg = LoginSuccess(cls.driver)
        lg.login()
        cls.um = UserManage_(cls.driver)

    def test_addMoney(self):
        '''成功充值储值金'''
        self.um.add_money()
        self.um.is_addMoneySucess()
    def test_reduceMoney(self):
        '''成功减扣储值金'''
        self.um.reduce_money()
        self.um.is_reduceMoneySucess()
    def test_aadIntegral(self):
        '''成功赠送积分'''
        self.um.add_integral()
        self.um.is_addIntegralSucess()
    def test_reduceInegral(self):
        '''成功减扣积分'''
        self.um.reduce_integral()
        self.um.is_reduceIntegralSucess()
    def test_giveVipCard(self):
        '''成功赠送会员卡'''
        self.um.give_VIPcard()
        self.um.is_addVipSucess()
    def test_giveCoupon(self):
        '''成功赠送优惠券'''
        self.um.give_coupon()
        self.um.is_giveCoupon()


    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()