#coding=utf-8
from common.base import Base
import time
from selenium import webdriver
from pages.login import LoginSuccess
class RoomManage(Base):
    '''行业预约房间管理'''
    #房间管理
    loc1=('xpath','//*[@id="container"]/div[2]/div/div/new-bookiing/div/new-booking-setting/div/div[2]/div/div/div[4]')
    #新增房间
    loc2=('xpath','//*[@id="container"]/div[2]/div/div/new-bookiing/div/new-booking-setting/div/div[2]/div'
                  '/worker-management/div/div[1]/div[1]/button[1]')
    #房间名称
    loc3=('id','name')
    #选择规格
    loc4=('xpath','//*[@id="container"]/div[2]/div/div/new-bookiing/div/people-manage/div/div[2]/nz-spin/div[2]/div[1]/form'
                  '/div[3]/div[2]/div/service-select/div[2]/nz-table/div/nz-spin/div[2]/div/div/div/div/div/table/tbody/tr[1]/td[1]/label/span/input')
    #添加图片
    loc5=('xpath','//*[@id="container"]/div[2]/div/div/new-bookiing/div/people-manage/div/div[2]/nz-spin/div[2]/div[1]/form/div[4]/div[2]/div/div/i')
    loc6=('xpath','/html/body/app/photo-modal/div/nz-modal[1]/div/div[2]/div[1]/div/div[2]/div[2]/nz-spin/div[2]/div/div/div[1]/img')
    loc7=('xpath','/html/body/app/photo-modal/photo-crop-modal/nz-modal/div/div[2]/div[1]/div/div[3]/div/button[1]')
    #保存
    loc8=('xpath','//*[@id="container"]/div[2]/div/div/new-bookiing/div/people-manage/div/div[2]/nz-spin/div[2]/div[2]/button[1]')
    #添加成功后的房间名称
    loc9=('xpath','//*[@id="container"]/div[2]/div/div/new-bookiing/div/new-booking-setting/div/div[2]/div/worker-management/div/div[3]/div/div[1]'
                  '/nz-table/div/nz-spin/div[2]/div/div/div/div/div/table/tbody/tr[1]/td[1]/div/label')
    #页面装修弹窗
    loc10=('xpath','/html/body/app/jisu-sider/div/nz-spin/div[2]/ul/li[4]/div[2]/span')

    def roommanage(self,roomname):
        self.driver.get('http://www.zhichiwangluo.com/management/shops/new-booking/setting/overview/2961?id=3cy3XO8rht')
        time.sleep(3)

        #判断页面装修弹窗是否在页面显示，当显示时点击
        if self.isDispalyed(self.loc10)== True:
            self.click(self.loc10)

        #点击房间管理
        self.click(self.loc1)
        #新增房间
        self.click(self.loc2)
        #添加房间信息
        self.sendKyes(self.loc3,roomname)
        self.click(self.loc4)
        self.js_focus(self.loc5)#使该元素滚动到页面可见
        self.click(self.loc5)
        self.click(self.loc6)
        self.click(self.loc7)
        #保存
        self.click(self.loc8)
    #判断是否添加成功
    def is_addroomsucess(self,_text):
        return self.is_text_in_element(self.loc9,_text)


if __name__ == '__main__':
           driver=webdriver.Chrome()
           log=LoginSuccess(driver)
           log.login()
           rm=RoomManage(driver)
           stime=time.strftime('%Y_%m_%d_%H_%M_%S')
           _text="标准间"+stime
           rm.roommanage(_text)
           result=rm.is_addroomsucess(_text)
           print(result)















