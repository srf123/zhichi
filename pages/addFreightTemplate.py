#coding=utf-8
from common.base import Base
from selenium import webdriver
from pages.login import LoginSuccess as lg
import time
class AddFreightTemplate(Base):
    '''添加运费模板'''
    #店铺设置
    loc1=('xpath','//*[@id="container"]/e-commerce/div[2]'
                  '/div[1]/inline-sider/nz-spin/div[2]/div/div/div/div[2]')
    #快递开关
    loc2=('xpath','//*[@id="container"]/e-commerce/div[2]/div[2]/e-commerce-shop-setting'
                  '/div/div/div/pick-setting/div/nz-spin/div[2]/div/div/div[1]/div[1]/nz-switch/span')
    #关闭快递时弹窗取消按钮
    loc2_1=('xpath','/html/body/nz-confirm/div/div[2]/div[1]/div/div/div/div[2]/button[1]')
    #快递设置
    loc3=('xpath','//*[@id="container"]/e-commerce/div[2]/div[1]'
                  '/inline-sider/nz-spin/div[2]/div/div/div/div[4]')

    #模板运费
    loc4=('xpath','//*[@id="container"]/e-commerce/div[2]/div[2]'
                  '/freight-management/div/div/nz-radio-group/label[3]/span[2]')

    #新建模板运费
    loc5=('xpaht','//*[@id="container"]/e-commerce/div[2]/div[2]/freight-management'
                  '/div/template-freight/div/div[1]/button[1]')


    #模板名称
    loc6=('xpath','//*[@id="container"]/e-commerce/div[2]/div[2]'
                  '/add-template/div/div[2]/form/div[1]/div[2]/nz-input/input')
    #模板类型(或按件数)
    loc7=('xpath','//*[@id="container"]/e-commerce/div[2]/div[2]/add-template'
                  '/div/div[2]/form/div[2]/div[2]/nz-radio-group/label[2]/span[2]')
    #模板类型(或按体积)
    loc8=('xpaht','//*[@id="container"]/e-commerce/div[2]/div[2]/add-template'
                  '/div/div[2]/form/div[2]/div[2]/nz-radio-group/label[3]/span[2]')

    #默认运费（n件/米以内距离）
    loc9=('xpath','//*[@id="container"]/e-commerce/div[2]/div[2]/add-template'
                  '/div/div[2]/form/div[3]/div[2]/input[1]')
    #默认运费（n件/米以内距离的价格）
    loc10=('xpath','//*[@id="container"]/e-commerce/div[2]/div[2]'
                   '/add-template/div/div[2]/form/div[3]/div[2]/input[2]')
    #默认运费（每次增加的件数/距离）
    loc11=('xpath','//*[@id="container"]/e-commerce/div[2]/div[2]/add-template'
                   '\/div/div[2]/form/div[3]/div[2]/input[3]')
    #默认运费（每次增加件数/距离后增加的金额）
    loc12=('xpath','//*[@id="container"]/e-commerce/div[2]/'
                   'div[2]/add-template/div/div[2]/form/div[3]/div[2]/input[4]')
    #满包邮设置下拉选
    loc13=('xpath','//*[@id="container"]/e-commerce/div[2]/div[2]/add-template'
                   '/div/div[2]/form/div[4]/div[2]/div/div/nz-select/div')
    #满包邮下拉选(不包邮)
    loc14=('xpath','//*[@id="cdk-overlay-5"]/div/div/ul/li[1]')
    #满包邮下拉选（按金额包邮）
    loc15=('xpath','//*[@id="cdk-overlay-5"]/div/div/ul/li[2]')
    #满包邮金额
    loc15_1=('xpath','//*[@id="container"]/e-commerce/div[2]/div[2]'
                     '/add-template/div/div[2]/form/div[4]/div[2]/div/div/div/input')
    #地区自定义包邮开关
    loc16=('xpath','//*[@id="container"]/e-commerce/div[2]/div[2]'
                   '/add-template/div/div[2]/form/div[5]/div[2]/div[1]/nz-switch/span')
    #添加可配送地区和运费
    loc17=('xpath','//*[@id="container"]/e-commerce/div[2]/div[2]/add-template/div/div[2]'
                   '/form/div[5]/div[2]/div[2]/nz-tag/span/span')
    #添加内蒙古区域
    loc18=('xpaht','//*[@id="container"]/e-commerce/div[2]/div[2]/add-template/area-setting/nz-modal'
                   '/div/div[2]/div[1]/div/div[2]/nz-spin/div[2]/div/div[2]/div[1]/ul/li[5]/label/span/input')
    #点击保存
    lolc19=('xpaht','//*[@id="container"]/e-commerce/div[2]/div[2]/add-template/area-setting/nz-modal'
                    '/div/div[2]/div[1]/div/div[3]/button[2]')
    #城市运费设置
    loc20=('xpath','//*[@id="container"]/e-commerce/div[2]/div[2]/add-template/div/div[2]/form/div[5]/div[2]/div[2]'
                   '/nz-table/div/nz-spin/div[2]/div/div/div/div/div/table/tbody/tr/th[2]/input')
    loc21=('xpath','//*[@id="container"]/e-commerce/div[2]/div[2]/add-template/div/div[2]/form/div[5]/div[2]/div[2]'
                   '/nz-table/div/nz-spin/div[2]/div/div/div/div/div/table/tbody/tr/th[3]')
    loc22=('xpath','//*[@id="container"]/e-commerce/div[2]/div[2]/add-template/div/div[2]/form/div[5]/div[2]/div[2]'
                   '/nz-table/div/nz-spin/div[2]/div/div/div/div/div/table/tbody/tr/th[4]/input')
    loc23=('xpath','//*[@id="container"]/e-commerce/div[2]/div[2]/add-template/div/div[2]/form/div[5]/div[2]/div[2]'
                   '/nz-table/div/nz-spin/div[2]/div/div/div/div/div/table/tbody/tr/th[5]')
    #点击保存
    loc24=('xpath','//*[@id="container"]/e-commerce/div[2]/div[2]/add-template/div/div[2]/form/div[6]/button[1]')
    #模板名称
    loc25=('xpath','//*[@id="container"]/e-commerce/div[2]/div[2]/freight-management/div'
                   '/template-freight/div/div[2]/div[1]/span[1]')
    def addfreighttemplate(self,nam):
        self.driver.get("http://www.zhichiwangluo.com/management/shops/e-commerce/goods/goods-list")
        time.sleep(3)
        self.click(self.loc1)
        #判断运费开关是否开启
        p=self.findElement(self.loc2).getAttribute('class')
        print("1111111"+p)
        self.click(self.loc2)
        # if self.isDispalyed(self.loc2_1)==True:
        #     self.click(self.loc2_1)

        time.sleep(3)
        self.click(self.loc3)

        self.click(self.loc4)
        #新建运费模板
        time.sleep(3)
        self.click(self.loc5)
        #模板名称
        self.sendKyes(self.loc6,nam)
        #判断件数类型有没有被选中
        if self.isSelected(self.loc7)==False:
            self.click(self.loc7)
        #默认运费
        self.sendKyes(self.loc9,1)
        self.sendKyes(self.loc10, 1)
        self.sendKyes(self.loc11, 1)
        self.sendKyes(self.loc12, 1)
        #判断满包邮条件是否按金额设置
        if self.isSelected(self.loc15) == False:
            self.click(self.loc13)
            self.click((self.loc15))
            self.sendKyes(self.loc15_1,10)

        #开启自定义包邮条件开关
            self.click(self.loc16)

        #添加可配送区域和运费
        self.click(self.loc17)
        #判断内蒙古是否被选中
        if self.isSelected(self.loc18) == False:
            self.click(self.loc18)
        self.click(self.loc19)
        self.click(self.loc20)
        self.click(self.loc21)
        self.click(self.loc22)
        self.click(self.loc23)
        self.click(self.loc24)


    #通过模板名称判断是否添加成
    def is_addFreightTempSuccess(self,_text):
        return self.is_text_in_element(self.loc25,_text)




if __name__ == '__main__':
    driver=webdriver.Chrome()
    lg(driver).login()
    add=AddFreightTemplate(driver)


    nam="运费模板"+time.strftime("%Y_%m_%d_%H_%M_%S")
    add.addfreighttemplate(nam)
    result=add.is_addFreightTempSuccess(nam)
    print(result)













