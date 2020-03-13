# # conding:utf-8
# from selenium import webdriver
# from ase import loginfc
# import unittest
# #添加商品判断是否添加成功1
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
import unittest
from pages import login


class Test_Login(unittest.TestCase):

    def setUp(self) -> None: #每个用例执行前先执行一次   ---实例方法
        self.lg= login.LoginSuccess

        self.driver=webdriver.Chrome()

        print("打开浏览器")



    def test_login(self):  #用例一
        '''用例说明：用户名密码正确，登录成功'''
        self.lg.login(self.driver,"13534050371","1133557799")



        '''日历控件readonly：当日历有readonly属性时只能选择时间，无法输入时间，先移除只读属性在赋值'''
        js = '''docunment.gentElementById("id").removeAttribute("readonly");
                docunment.gentElementById("id").value="2019-9-20"
               '''
        self.driver.execute_script(js)


    def tearDown(self) -> None:  #用例执行完后，调用一次
        self.driver.delete_all_cookies() #清空cookies退出登录
        self.driver.refresh()   #刷新页面
        self.driver.quit()

        print("关闭浏览器")
