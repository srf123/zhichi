#coding-utf-8
from selenium import webdriver
import time
import unittest
from pages.login import LoginSuccess


class Test_Login(unittest.TestCase):
    # '''登录类用例'''
    @classmethod  #--类方法用classmethod修饰
    def setUpClass(cls) -> None: #用例执行前，先执行一次  ---类方法
        cls.driver = webdriver.Chrome()
        cls.lg = LoginSuccess(cls.driver)

    def setUp(self) -> None: #每个用例执行前先执行一次   ---实例方法
        self.driver.get("http://www.zhichiwangluo.com/index.php?r=login/Ulogin")
        # self.driver.maximize_window()  # 最大化
        # url = "http://www.zhichiwangluo.com"
        # self.driver.get(url)
        print("打开浏览器")

    def test_01(self):  #用例一
        '''用例说明：输入正确的用户名密码，登录成功'''
        self.lg.input_user("18919045147")
        self.lg.input_password("123456")
        self.lg.click_login_button()

        #self.lg.login("18919045147","123456")
        # p = self.driver.find_element_by_class_name("pic-code getPicCode").text
        # print(p)
        #判断是否登录成功
        time.sleep(3)
        t = self.lg.get_login_username()#获取登录后的用户名
        print(t)
        self.assertTrue(t == "毝毝蟲")  # unittest自带的断言，判断实际结果和预期结果是否相等

    def test_02(self):#用例二   错误为空
        '''用例说明：用户名正确、密码为空，登录失败'''
        # # 点击登录
        #         # self.driver.find_element_by_xpath("//a[@class='nav-login-btn']").click()
        #         # time.sleep(3)
        #         # # 获取所有窗口的句柄
        #         # handles = self.driver.window_handles
        #         # print(handles)
        #         # # 通过句柄切换到当前窗口
        #         # self.driver.switch_to_window(handles[2])
        #         # time.sleep(3)
        self.lg.input_user("18919045147")
        self.lg.input_password("")
        self.lg.click_login_button()
        # self.lg.login("18919045147","")
        # 判断是否登录成功
        time.sleep(3)
        t = self.lg.get_login_username()
        print(t)
        print("登录失败，用户名为空:%s"%t)
        self.assertTrue(t == "")  # unittest自带的断言，断言失败自动截图

    def test_03(self):  # 用例3
            '''用例说明：用户名正确、密码为正确，点击自动登录,点登录'''
            self.lg.input_user("18919045147")
            self.lg.input_password("123456")
            self.lg.click_keep_login()
            self.lg.click_login_button()
            # 判断是否登录成功
            time.sleep(3)
            t = self.lg.get_login_username()
            print(t)
            self.assertTrue(t == "毝毝蟲")  # unittest自带的断言，断言失败自动截图
    def test_04(self):
        '''点击忘记密码'''
        self.lg.forget_pass()
        pa=self.lg.is_input_admin()
        print(pa)
        self.assertTrue(pa == "1.填写账号")




    def tearDown(self) -> None:  #用例执行完后，调用一次
        self.driver.delete_all_cookies() #清空cookies退出登录
        self.driver.refresh()   #刷新页面
        #self.driver.quit()

        print("关闭浏览器")

    @classmethod
    def tearDownClass(cls) -> None:  # 用例执行后，执行一次"
        cls.driver.quit()

    #     print("用例后，只执行一次")