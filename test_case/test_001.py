#coding-utf-8
from selenium import webdriver
import time
import unittest
from test_case import loginfc
class Test_Login(unittest.TestCase):
    # '''登录类用例'''
    # @classmethod  #--类方法用classmethod修饰
    # def setUpClass(cls) -> None: #用例执行前，先执行一次  ---类方法
    #     cls.driver = webdriver.Chrome()
    #
    #     print("用例前，只执行一次")
    #
    #
    def setUp(self) -> None: #每个用例执行前先执行一次   ---实例方法
        self.lg=loginfc.LoginSuccess

        #         self.driver.maximize_window()  # 最大化
        # url = "http://www.zhichiwangluo.com"
        # self.driver.get(url)
        self.driver=webdriver.Chrome()

        print("打开浏览器")

    # @classmethod
    # def tearDownClass(cls) -> None:  # 用例执行后，执行一次"
    #     cls.driver.quit()
    #
    #     print("用例后，只执行一次")

    def tearDown(self) -> None:  #用例执行完后，调用一次
        self.driver.delete_all_cookies() #清空cookies退出登录
        self.driver.refresh()   #刷新页面
        self.driver.quit()

        print("关闭浏览器")



    # def login(self,username,password):
    #     #登录方法
    #      self.driver.find_element_by_id("login-username").send_keys(username)
    #      self.driver.find_element_by_id("login-password").send_keys(password)
    #      time.sleep(3)
    #      self.driver.find_element_by_xpath("//div[@class='submit-btn']").click()

    def test_login(self):  #用例一
        '''用例说明：用户名密码正确，登录成功'''


        self.lg.login(self.driver,"13534050371","1133557799")

        # p = self.driver.find_element_by_class_name("pic-code getPicCode").text
        # print(p)

        #判断是否登录成功
        time.sleep(3)

        # if t== "毝毝蟲":
        #     print("pass")
        # else:
        #     print("fail")
        t = self.lg.get_login_username()
        self.assertTrue(t == "毝毝蟲")  # unittest自带的断言，判断实际结果和预期结果是否相等

    def test_password_wrong(self):#用例二   错误密码
        '''用例说明：用户名正确、密码错误，登录失败'''
        # # 点击登录
        #         # self.driver.find_element_by_xpath("//a[@class='nav-login-btn']").click()
        #         # time.sleep(3)
        #         # # 获取所有窗口的句柄
        #         # handles = self.driver.window_handles
        #         # print(handles)
        #         # # 通过句柄切换到当前窗口
        #         # self.driver.switch_to_window(handles[2])
        #         # time.sleep(3)
        self.lg.login(self.driver,"13534050371","123123")
        # 判断是否登录成功
        time.sleep(3)
        t = self.lg.get_login_username()
        print("登录失败，用户名为空:%s"%t)
        self.assertTrue(t == "")  # unittest自带的断言，断言失败自动截图



