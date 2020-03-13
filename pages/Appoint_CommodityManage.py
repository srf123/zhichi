#coding:utf-8
from common.base import Base
import time
from selenium import webdriver
from pages.login import LoginSuccess
import time
class CommodityManage(Base):
    '''行业预约商品管理'''
    # 页面装修弹窗
    loc1 = ('xpath', '/html/body/app/jisu-sider/div/nz-spin/div[2]/ul/li[4]/div[2]/span')
    #商品管理菜单
    loc2=('xpath','//*[@id="container"]/div[2]/div/div/new-bookiing/div/new-booking-setting/div/div[2]/div/div/div[5]')
    #添加商品按钮
    loc3=('xpath','//*[@id="container"]/div[2]/div/div/new-bookiing/div/new-booking-setting/div/div[2]'
                  '/div/goods-management/div/div[1]/button')
    #商品名称
    loc4=('xpath','//*[@id="container"]/div[2]/div/div/new-bookiing/div/new-booking-setting/div/div[2]/div/goods-operation/nz-content/div/div[2]/div/div[1]/div[2]/input')
    #选择规格
    loc5=('xpath','//*[@id="container"]/div[2]/div/div/new-bookiing/div/new-booking-setting/div/div[2]/div/goods-operation/nz-content/div/div[2]/div/div[2]/div[2]'
                  '/service-select/div[2]/nz-table/div/nz-spin/div[2]/div/div/div/div/div/table/tbody/tr[1]/td[1]/label/span/input')
    #添加商品图片
    loc6=('xpath','//*[@id="container"]/div[2]/div/div/new-bookiing/div/new-booking-setting/div/div[2]/div/goods-operation/nz-content/div/div[2]/div/div[5]/div[2]/div')
    loc7=('xpath','/html/body/app/photo-modal/div/nz-modal[1]/div/div[2]/div[1]/div/div[2]/div[2]/nz-spin/div[2]/div/div/div[1]/img')
    loc8=('xpath','/html/body/app/photo-modal/photo-crop-modal/nz-modal/div/div[2]/div[1]/div/div[3]/div/button[1]')
    #商品描述
    loc9=('id','ueditor_0')
    loc10=('xpath','/html/body')
    #确定
    loc11=('xpath','//*[@id="container"]/div[2]/div/div/new-bookiing/div/new-booking-setting/div/div[2]/div/goods-operation/nz-content/div/div[3]/button[1]')
    #添加后的商品名称
    loc12=('xpath','//*[@id="container"]/div[2]/div/div/new-bookiing/div/new-booking-setting/div/div[2]/div/goods-management/nz-spin/div[2]/div/nz-table/div'
                   '/nz-spin/div[2]/div/div/div/div/div/table/tbody/tr[1]/td[1]')
    def add_commodity(self,commname="预约商品"):
        '''添加商品'''
        self.driver.get('http://www.zhichiwangluo.com/management/shops/new-booking/setting/overview/4254?id=EQBYDcBill')
        time.sleep(2)
        if self.isDispalyed(self.loc1)==True:
            self.click(self.loc1)
        self.click(self.loc2)
        self.click(self.loc3)
        time.sleep(2)
        self.click(self.loc4)
        self.sendKyes(self.loc4,commname)
        print("-----------------------")
        if self.isSelected(self.loc5)==False:
            self.click(self.loc5)
        self.js_focus(self.loc6)
        self.click(self.loc6)
        self.click(self.loc7)
        self.click(self.loc8)
        self.iframe(self.loc9)#切换到iframe上
        print('=========================')
        self.sendKyes(self.loc10,commname)
        #退出iframe
        self.quit_iframe()
        self.click(self.loc11)

    def is_addCommodifySucess(self,_text):
        return self.is_text_in_element(self.loc12,_text)

if __name__ == '__main__':
    driver=webdriver.Chrome()
    lg=LoginSuccess(driver)
    lg.login()
    cm=CommodityManage(driver)
    sname=time.strftime("%Y_%m_%d_%H_%M_%S")
    commname='预约商品'+sname
    cm.add_commodity(commname)
    result=cm.is_addCommodify(commname)
    print(result)







































