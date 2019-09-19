# conding:utf-8
#from selenium import webdriver
# from pages import loginfc
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


#查找元素

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait #导入WebDriverWait等待
from selenium.webdriver.common.by import By  #导入公共的元素查找方法By
'''
Example:
from selenium.webdriver.support.ui import WebDriverWait \n
element = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id("someId")) \n
is_disappeared = WebDriverWait(driver, 30, 1, (ElementNotVisibleException)).\ \n
until_not(lambda x: x.find_element_by_id("someId").is_displayed())
'''
driver = webdriver.Chrome()
driver.get("http://www.zhichiwangluo.com/index.php?r=login/Ulogin")
#element =WebDriverWait(driver,10).until(lambda x: x.find_element_by_id("someId"))

#共10s，每隔1s查找一次，只要定位到就结束
# element1 =WebDriverWait(driver,10,1).until(lambda x: x.find_element_by_id("login-username"))
# #返回的是element元素对象
# print(element1)
# element1.send_keys("18919045147")
# element2 =WebDriverWait(driver,10,1).until(lambda x: x.find_element_by_id("login-password"))
# element2.send_keys("123456")
# element3 =WebDriverWait(driver,10,1).until(lambda x: x.find_element_by_class_name("submit-btn"))
# element3.click()

#公共查找方法
# driver.find_element(By.ID,"login-username")
# driver.find_element(By.ID,"login-password")
# driver.find_element(By.CLASS_NAME,"submit-btn")

#封装元素定位方法

def findElement(driver,loctor,timeout=10,t=0.5):
    element = WebDriverWait(driver, timeout, t).until(lambda x: x.find_element(*loctor))
    return element


loctor1=(By.ID,"login-username")
loctor2=(By.ID,"login-password")
loctor3=(By.CLASS_NAME,"submit-btn")

loc1 = ("id", "login-username")
loc2 = ("css selector", "[id=login-password]")
loc3 = ("xpath", "//*[@id='login-btn']")

findElement(driver,loctor1).send_keys("18919045147")
findElement(driver,loctor2).send_keys("123456")
findElement(driver,loctor3).click()