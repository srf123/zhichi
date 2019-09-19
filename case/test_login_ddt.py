#coding-utf-8
from selenium import webdriver
import time
import unittest
from pages.login import LoginSuccess
import ddt
from common.read_excel import ExcelUtil
import os
'''
1、输入正确的用户名密码，登录成功s
2、用户名正确、密码为空，登录失败
3、用户名错误、密码正确、登录失败

'''
#将测试数据放到list中用字典存储
# testdates = [
#     {"user":"18919045147","pasw":"123456","expect":"毝毝蟲"},
#     {"user":"18919045147","pasw":"","expect":""},
#     {"user":"1891904514","pasw":"123456","expect":""}
# ]


#通过test_login_ddt路径找到untitled工程路径
propath =os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
#通过工程路径找到datas路径
filepath = os.path.join(propath ,"common","datas.xls")
print(filepath)
data = ExcelUtil(filepath)
testdates=data.dict_data()
print (testdates)



@ddt.ddt
class Test_Login(unittest.TestCase):
    # '''登录类用例'''
    @classmethod  #--类方法用classmethod修饰
    def setUpClass(cls) -> None: #用例执行前，先执行一次  ---类方法
        cls.driver = webdriver.Chrome()
        cls.lg = LoginSuccess(cls.driver)

    def setUp(self) -> None: #每个用例执行前先执行一次   ---实例方法
        self.driver.get("http://www.zhichiwangluo.com/index.php?r=login/Ulogin")
        print("打开浏览器")

    def login_case(self,user,pasw,expect):#用户名、密码、断言
         self.lg.input_user(user)
         self.lg.input_password(pasw)
         self.lg.click_login_button()
         # 判断是否登录成功
         time.sleep(3)
         t = self.lg.get_login_username()  # 获取登录后的用户名
         print(t)
         self.assertTrue(t == expect)  # unittest自带的断言，判断实际结果和预期结果是否相等

    @ddt.data(*testdates)
    def test_01(self,data):  #使用ddt框架，三个用例可以写在一个方法中
        '''用例说明：输入正确的用户名密码，登录成功'''
        self.login_case(data["user"],data["pasw"],data["expect"])


    def tearDown(self) -> None:  #用例执行完后，调用一次
        self.driver.delete_all_cookies() #清空cookies退出登录
        self.driver.refresh()   #刷新页面

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()


