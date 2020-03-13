#coding=utf-8
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait #导入WebDriverWait等待
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import time


class Base():#基础操作封装
    '''公共的参数封装'''


    def __init__(self,driver:webdriver.Chrome):
        self.driver=driver
        self.timeout=15
        self.t=0.5
    #元素定位
    def findElementNew(self,locator):
         """定位到元素，返回元素对象，没有定位到，抛TImeout异常"""
         element=WebDriverWait(self.driver,self.timeout,self.t).until(EC.presence_of_element_located(locator))
         return element

    #封装元素定位方法
    def findElement(self,locator):
        try:
            if not isinstance(locator,tuple):
                print("locator参数类型错误，必须为元祖类型：loc=('id','value')")
            else:
                print("正在定位元素信息：定位方式—>%s，value值->%s"%(locator[0],locator))
                element = WebDriverWait(self.driver, self.timeout, self.t).until(lambda x: x.find_element(*locator))
                return element
        except:
            return "定位失败"
    # 封装定位一组元素
    def findElements(self, locator):
        try:
            elements = WebDriverWait(self.driver, self.timeout, self.t).until(lambda x: x.find_elements(*locator))
            return elements
        except:
            return "查找超时"

    #封装send_keys
    def sendKyes(self,locator,_text):
        element = self.findElement(locator)
        element.send_keys(_text)


    #封装click
    def click(self,locator):
        element = self.findElement(locator)
        element.click()

    #封装claer
    def cleat(self,locator):
        element = self.findElement(locator)
        element.clear()

    #判断是否被选中
    def isSelected(self,locator):
        element = self.findElement(locator)
        sele = element.is_selected()
        return sele

     # 判断元素是否在页面显示
    def isDispalyed(self, locator):
        element = self.findElement(locator)
        sele = element.is_displayed()
        return sele

    #判断元素是否可以使用
    def isEnabled(self, locator):
        element = self.findElement(locator)
        sele = element.is_enabled()
        return sele


    #判断元素是否存在:方法一
    def isElementExist(self,locator):
        try:
            element = self.findElement(locator)
            return  element
        except:
            return False

    #方法二
    def isElementExist2(self, locator):
        element2=self.findElement(locator)
        n = len(element2)
        if n == 0:
            return  False
        elif n == 1:
            return True
        else:
            print("定位到多个")
            return True


     #title_is当前页面的title是否完全等于（==）预期字符串,断言（预期结果）（driver）,
    def is_title(self,_title):
        #返回bool值
        try:
            result= WebDriverWait(self.driver, self.timeout, self.t).until(EC.title_is(_title))
            return result
        except:
            return False

     # title_contains当前页面的title是否包含预期字符串,断言（预期结果）（driver）,
    def title_contains(self, _title):
        # 返回bool值
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.title_contains(_title))
            return result
        except:
            return False

    #text_to_be_present_in_element判断某个元素中的text是否包含了预期的字符串
    def is_text_in_element(self,locator,_text):
        # 返回bool值
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.text_to_be_present_in_element(locator,_text))
            return result
        except:
            return False

    #text_to_be_present_in_element_valu判断某个元素中的value是否包含了预期的字符串
    def is_value_in_element(self,locator,value):
        # 返回bool值，value为空字符串返回false
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.text_to_be_present_in_element_value(locator,value))
            return result
        except:
            return False

    #判断是否有alert弹窗，有返回alert对象，没有返回false
    def is_alert(self):
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.alert_is_present())
            return result
        except:
            return False

     #鼠标悬停
    def move_to_element(self,locator):
        ele=self.findElement(locator)
        ActionChains(self.driver).move_to_element(ele).perform()


    #切换到iframe上
    def iframe(self,locator):
        self.driver.switch_to_frame(self.findElement(locator))
    #从iframe切换到主页面
    def quit_iframe(self):
        self.driver.switch_to.default_content()

    #从iframe切换到上一级iframe，当只有一级iframe时，不支持切换到主页面
    def ifrmae_parent(self):
        self.driver.switch_to.parent_frame()


    #tselect通过下标定位选中
    def select_by_index(self,locator,index=0):
        '''通过索引，index是索引第几个，从0开始，默认选中第一个'''
        ele=self.findElement(locator)
        Select(ele).select_by_index(index)

    #通过value值定位选中
    def select_by_value(self, locator,value):
        ele = self.findElement(locator)
        Select(ele).select_by_value(value)

    # 通过文本值定位选中
    def select_by_value(self, locator,text):
        ele = self.findElement(locator)
        Select(ele).select_by_visible_text(text)

     #滚动条操作，聚焦元素，使元素出现在页面可见范围
    def js_focus(self,locator):
        target = self.findElement(locator)
        self.driver.execute_script("arguments[0].scrollIntoView()",target)

    # 获取表格行数tr的长度，用于定位table中最后一行的下标
    def lasttable(self,locator,tr):
        tbody = self.findElement(locator)
        tr = tbody.find_elements_by_tag_name(tr)
        return str(len(tr))  # 转换为字符串

    #分页中，获取最后一页的下标
    def lastpages(self,locator):
        # 通过获取ul下li的长度，获取最后一页的下标
        ul = self.findElement(locator)
        li = ul.find_elements_by_tag_name("li")
        return str(len(li) - 1)

    #根据元素属性值
    def Attribute(self,locator,attb):
        self.tager=self.findElement(locator)
        return self.tager.get_attribute(attb)

    #获取td文本值
    def td_text(self,locator):
       self.td= self.findElement(locator)
       return self.td.text
    #清空文本框内容
    def clear(self,locator):
        self.findElement(locator).clear()










if __name__ == '__main__':
      driver=webdriver.Chrome()
      driver.get("http://www.zhichiwangluo.com/index.php?r=login/Ulogin")
      bs=Base(driver)
      # loc1 = (By.ID, "login-username")
      # loc2=(By.CSS_SELECTOR, "[id=login-password]")
      # loc3=(By.XPATH, "//*[@id='login-btn']")
      loc1=("id","login-username")
      loc2=("css selector","[id=login-password]")
      loc3=("xpath","//*[@id='login-btn']")
      loc4 = ("id", "save-PW")
      bs.sendKyes(loc1,"18919045147")
      bs.sendKyes(loc2,"123456")
      bs.click(loc4)
      b=bs.isSelected(loc4)
      print(b)
      bs.click(loc3)
      driver.get('http://www.zhichiwangluo.com/management/marketing'
                 '/distribution/distribution-rule-management/distribution-rule-management-rule?id=EQBYDcBill')
      # 页面装修弹窗
      loc5=('xpath', '/html/body/app/jisu-sider/div/nz-spin/div[2]/ul/li[4]/div[2]/span')
      loc6=('xpath','//*[@id="container"]/div[2]/div[2]/div[2]/marketing/nz-layout/nz-layout/distribution-promotion/div'
                    '/distribution-rule-management/rule-setting/nz-spin/div[2]/form/div[2]/div/p[1]/span[2]/div/nz-switch/span')
      time.sleep(2)
      bs.click(loc5)

      ab=bs.Attribute(loc6)
      print(ab)

