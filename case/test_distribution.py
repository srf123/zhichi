#coding:utf-8
from selenium import webdriver
import unittest
from pages.login import LoginSuccess
from pages.distribution import Distribuiton
class Test_Distribution(unittest.TestCase):
    '''分销'''
    @classmethod
    def setUp(self) -> None:
        self.driver=webdriver.Chrome()
        ls=LoginSuccess(self.driver)
        ls.login()
        self.dt=Distribuiton(self.driver)
    def test_distribution_rule_sucess(self):
        ''' 分销规则添加成功'''
        self.dt.distributionRule(30,20)
        _text="保存成功"
        result=self.dt.is_distrition_rule_sucess(_text)
        self.assertTrue(result)
    def test_distribution_rule_fail(self):
        '''分销规则添加失败：佣金超出限制'''
        self.dt.distributionRule(40,50)
        _text='佣金比例需大于等于0'
        result=self.dt.is_distrition_rule_sucess(_text)
        self.assertTrue(result)
    def test_distribution_rule_error(self):
        '''分销规则添加失败：佣金比例不合法'''
        self.dt.distributionRule(-1,20)
        _text='佣金比例需大于等于0'
        result = self.dt.is_distrition_rule_sucess(_text)
        self.assertTrue(result)
    def test_distrbution_rule_commission_null(self):
        '''分销规则添加失败：佣金比例为空'''
        self.dt.distributionRule("",'')
        _text="设置保存成功"
        result=self.dt.is_distrition_rule_sucess(_text)
        self.assertFalse(result)



    @classmethod
    def tearDown(self) -> None:
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()