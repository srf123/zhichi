#coding:utf-8
from selenium import webdriver
from common.base import Base
import time

login_url="http://www.zhichiwangluo.com/index.php?r=login/Ulogin"
class LoginSuccess(Base):
        loc_user = ("id", "login-username")#用户名
        loc_pass = ("id", "login-password")#密码
        loc_button = ("xpath", "//div[@class='submit-btn']")#登录按钮
        loc_keep = ("id","save-PW")#7天内自动登录
        loc_forget = ("id", "forget-PW")  # 忘记密码
        loc_add_admin = ("id", "to-reg")  # 注册账号
        loc_login_success_user= ("css selector", '.nickName')  # 登录后获取的用户名
        loc_input_admin = ("class name" ,"login_fill_in")

        #输入用户名
        def input_user(self,text):
                self.sendKyes(self.loc_user,text)

        # 输入密码
        def input_password(self, paw):
                self.sendKyes(self.loc_pass, paw)
        #点击登录
        def click_login_button(self):
                self.click(self.loc_button)
        #点击7天自动登录
        def click_keep_login(self):
                self.click(self.loc_keep)
         #注册账号
        def add_admin(self):
                self.click(self.add_admin())
         #忘记密码
        def forget_pass(self):
                self.click(self.loc_forget)

        #点击忘记密码跳转放到找回密码页面判断填写账号是否存在
        def is_input_admin(self):
                try:
                        ad= self.findElement(self.loc_input_admin).text
                        return ad
                except:
                        return ""


        #登录流程
        def login(self,username="18919045147",password="123456",keep_login=False):
                self.driver.get(login_url)
                self.driver.maximize_window()#放大窗口
                # self.driver.find_element_by_xpath("//a[@class='nav-login-btn']").click()
                # time.sleep(3)
                # # 获取所有窗口的句柄
                # handles = self.driver.window_handles
                # print(handles)
                # # 通过句柄切换到当前窗口
                # self.driver.switch_to_window(handles[1])
                self.sendKyes(self.loc_user, username)
                self.sendKyes(self.loc_pass, password)
                # 给一个keep_login参数默认值为False，当传入的值为true时，执行click_keep_login()
                if keep_login:
                        self.click_keep_login()
                self.click(self.loc_button)

        def get_login_username(self):
                # 获取登录成功后的用户名
                try:
                        t = self.findElement(self.loc_login_success_user).text  # css定位：id用#  class用.
                        print(t)
                        return t
                except:
                        return ""

#
# if __name__ == '__main__':
#       driver=webdriver.Chrome()
#       ls = LoginSuccess(driver)
#       ls.login()
if __name__ == '__main__':
        driver = webdriver.Chrome()
        driver.get(login_url)
        ls = LoginSuccess(driver)
        ls.input_user("18919045147")
        ls.input_password("123456")
        ls.click_keep_login()
        ls.forget_pass()
        p=ls.is_input_admin()
        print(p)


        # ls.click_login_button()