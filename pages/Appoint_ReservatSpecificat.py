#coding=utf-8
from common.base import Base
from selenium import webdriver
import time
import unittest
from pages.login import LoginSuccess
class Reseevatspceificat(Base):
    '''行业预约规格设置'''
    lilen=''
    #规格设置
    loc1=('xpath','//*[@id="container"]/div[2]/div/div/new-bookiing/div/new-booking-setting/div/div[2]/div/div/div[3]')
    #编辑规格
    loc2=('xpath','//*[@id="container"]/div[2]/div/div/new-bookiing/div/new-booking-setting/div/div[2]/div/service-setting/div/div/button[1]')
    #添加一级规格
    loc3=('xpath','//*[@id="container"]/new-bookiing/div[2]/div/new-booking-setting/div/div[2]/div'
                  '/service-setting/div/nz-spin/div[2]/div/div[2]/ul/li['+lilen+']/button')
    loc4=('xpath','//*[@id="container"]/new-bookiing/div[2]/div/new-booking-setting/div/div[2]/div'
                  '/service-setting/div/nz-spin/div[2]/div/div[2]/ul/li[5]/input-with-submit/a[1]/i')
    #一级规格价格
    loc5=('xpath','//*[@id="container"]/new-bookiing/div[2]/div/new-booking-setting/div/div[2]/div'
                  '/service-setting/div/nz-spin/div[2]/div/div[3]/nz-table/div/nz-spin/div[2]/div/div/div/div/div/table/tbody/tr[1]/td[3]/input-with-submit/input')

    loc6=('xpath','//*[@id="container"]/new-bookiing/div[2]/div/new-booking-setting/div/div[2]/div/service-setting/div/nz-spin/div[2]/div/div[3]/nz-table'
                  '/div/nz-spin/div[2]/div/div/div/div/div/table/tbody/tr[1]/td[3]/input-with-submit/a[1]')
    #添加二级规格
    loc7=('xpath','//*[@id="container"]/new-bookiing/div[2]/div/new-booking-setting/div/div[2]/div/service-setting/div/nz-spin/div[2]/div/div[3]/nz-table/div/'
                 'nz-spin/div[2]/div/div/div/div/div/table/tbody/tr[1]/td[1]/div/div/button')

    loc8=('xpath','//*[@id="container"]/new-bookiing/div[2]/div/new-booking-setting/div/div[2]/div/service-setting/div/nz-spin/div[2]/div/div[3]/nz-table/div/'
                  'nz-spin/div[2]/div/div/div/div/div/table/tbody/tr[1]/td[1]/div/div/input-with-submit/a[1]/i')
    #二级规格价格
    loc9=('xpath','//*[@id="container"]/new-bookiing/div[2]/div/new-booking-setting/div/div[2]/div/service-setting/div/nz-spin/div[2]/div/div[3]/nz-table/div/'
                  'nz-spin/div[2]/div/div/div/div/div/table/tbody/tr[1]/td[3]/input-with-submit/input')
    loc10=("xpath",'//*[@id="container"]/new-bookiing/div[2]/div/new-booking-setting/div/div[2]/div/service-setting/div/nz-spin/div[2]/div/div[3]/nz-table/div/' 
                       'nz-spin/div[2]/div/div/div/div/div/table/tbody/tr[1]/td[3]/input-with-submit/a[1]/i')
    #添加三级规格
    loc11=('xpath','//*[@id="container"]/new-bookiing/div[2]/div/new-booking-setting/div/div[2]/div/service-setting/div/nz-spin/div[2]/div/div[3]/nz-table/div'
                   '/nz-spin/div[2]/div/div/div/div/div/table/tbody/tr[1]/td[2]/div/button')
    loc12=('xpaht','//*[@id="container"]/new-bookiing/div[2]/div/new-booking-setting/div/div[2]/div/service-setting/div/nz-spin/div[2]/div/div[3]/nz-table/div/'
                   'nz-spin/div[2]/div/div/div/div/div/table/tbody/tr[1]/td[2]/div/input-with-submit/a[1]/i')
    #三级规格价格
    loc13=('xoath','//*[@id="container"]/new-bookiing/div[2]/div/new-booking-setting/div/div[2]/div/service-setting/div/nz-spin/div[2]/div/div[3]/nz-table/div'
                   '/nz-spin/div[2]/div/div/div/div/div/table/tbody/tr[1]/td[3]/input-with-submit/input')
    loc14=('xpath','//*[@id="container"]/new-bookiing/div[2]/div/new-booking-setting/div/div[2]/div/service-setting/div/nz-spin/div[2]/div/div[3]/nz-table/div'
                   '/nz-spin/div[2]/div/div/div/div/div/table/tbody/tr[1]/td[3]/input-with-submit/a[1]')
    #完成
    loc15=('xpath','//*[@id="container"]/new-bookiing/div[2]/div/new-booking-setting/div/div[2]/div/service-setting/div/div/button[1]')
    #添加成功后一级规格名称
    loc16=('xpath','//*[@id="container"]/new-bookiing/div[2]/div/new-booking-setting/div/div[2]/div/service-setting/div'
                   '/nz-spin/div[2]/div/div[2]/ul/li['+lilen+']')
    #新添加二级规格
    loc17=('xpath','//*[@id="container"]/new-bookiing/div[2]/div/new-booking-setting/div/div[2]/div/service-setting/div/nz-spin/div[2]/div/div[3]/nz-table'
                   '/div/nz-spin/div[2]/div/div/div/div/div/table/tbody/tr[1]/td[1]/div')
    # 页面装修弹窗
    loc18 = ('xpath', '/html/body/app/jisu-sider/div/nz-spin/div[2]/ul/li[4]/div[2]/span')
    def reservatSpecificat(self,stime):
        self.driver.get('http://www.zhichiwangluo.com/management/shops/new-booking/setting/overview/2961?id=3cy3XO8rht')
        time.sleep(3)
        # 判断页面装修弹窗是否在页面显示，当显示时点击
        if self.isDispalyed(self.loc18) == True:
            self.click(self.loc18)

        # 点击导航规格设置
        self.click(self.loc1)
        #点击编辑
        time.sleep(2)
        print(6666)
        self.click(self.loc2)
        #点击一级规格
        self.lilen=self.lasttable(self.loc3,"li")
        print("li长度"+self.lilen)
        self.sendKyes(self.loc3,"南山"+stime)
        self.click(self.loc4)
        #一级规格价格
        self.sendKyes(self.loc5,1)
        self.click(self.loc6)
        #二级规格
        self.click(self.loc7)
        self.sendKyes(self.loc7,'标准间'+stime)
        self.click(self.loc8)
        #二级规格价格
        self.sendKyes(self.loc9)
        self.click(self.loc10)
        #三级规格
        self.click(self.loc11)
        self.sendKyes(self.loc11, '有窗' )
        self.click(self.loc12)
        #三级规格价格
        self.sendKyes(self.loc13)
        self.click(self.loc14)
        #完成
        self.click(self.loc15)
    #判断一级规格是否添加成功
    def is_ReservatspecificatOne(self,_text):
        self.lilen = self.lasttable(self.loc3, "li")-1
        print("bbb" + self.lilen)
        return self.is_text_in_element(self.loc16,_text)
    #判断二级规格是否添加成功
    def is_ReservatSpecificatTwo(self,_text):
        return self.is_text_in_element(self.loc17._text)



if __name__ == '__main__':
    driver=webdriver.Chrome()
    log=LoginSuccess(driver)
    log.login()
    rs = Reseevatspceificat(driver)
    stime = time.strftime('%Y_%m_%d_%H_%M_%S')
    rs.reservatSpecificat(stime)
    result=rs.is_Reservatspecificat(stime)
    print((result))















