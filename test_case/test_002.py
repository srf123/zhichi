# # conding:utf-8
# from selenium import webdriver
# from test_case import loginfc
# import unittest
# #添加商品判断是否添加成功
#
# class TJ(unittest.TestCase):
#     def setUp(self) -> None:
#         self.lg=loginfc.LoginSuccess
#         self.driver=webdriver.Chrome()
#         print("222")
#
#     # def __init__(self,driver):
#     #     self.driver=driver
#
#     def test_loginf(self):
#         self.lg.login(self.driver,'18919045147','123456')
#         print("111")





#coding-utf-8
from selenium import webdriver
import time
import unittest
from test_case import loginfc
class Test_Login(unittest.TestCase):

    def setUp(self) -> None: #每个用例执行前先执行一次   ---实例方法
        self.lg=loginfc.LoginSuccess

        self.driver=webdriver.Chrome()

        print("打开浏览器")



    def tearDown(self) -> None:  #用例执行完后，调用一次
        self.driver.delete_all_cookies() #清空cookies退出登录
        self.driver.refresh()   #刷新页面
        self.driver.quit()

        print("关闭浏览器")




    def test_login(self):  #用例一
        '''用例说明：用户名密码正确，登录成功'''


        self.lg.login(self.driver,"13534050371","1133557799")



