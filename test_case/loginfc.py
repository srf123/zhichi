#conding=utf-8
from selenium import webdriver
import  time
class LoginSuccess():
        def __init__(self,driver):  #定义全局变量
                self.driver = driver

        def login(self,username=18919045147,password=123456):
                self.driver.get("http://www.zhichiwangluo.com")
                self.driver.maximize_window()#放大窗口
                self.driver.find_element_by_xpath("//a[@class='nav-login-btn']").click()
                time.sleep(3)
                # 获取所有窗口的句柄
                handles = self.driver.window_handles
                print(handles)
                # 通过句柄切换到当前窗口
                self.driver.switch_to_window(handles[1])

                self.driver.find_element_by_id("login-username").send_keys(username)
                self.driver.find_element_by_id("login-password").send_keys(password)
                self.driverr.find_element_by_xpath("//div[@class='submit-btn']").click()



        def get_login_username(self):
                # 获取登录成功后的用户名
                try:
                        t = self.driver.find_element_by_css_selector(".nickName").text  # css定位：id用#  class用.
                        print(t)
                        return t
                except:
                        return ""


        if __name__ == '__main__':
              driver=webdriver.Chrome()
              login(driver)