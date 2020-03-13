#coding:utf-8
from common.base import Base
from pages.login import LoginSuccess
from selenium import webdriver
class Distribuiton(Base):
    '''分销'''

    #二级分销
    loc1=('xpath','//*[@id="container"]/div[2]/div[2]/div[2]/marketing/nz-layout/nz-layout/distribution-promotion/div/distribution-rule-management/distribution-rule-setting/rule-setting/nz-spin/div[2]/form/div[1]/div/p[1]/span[2]')
    #佣金比例
    loc2=('xpath','//*[@id="container"]/div[2]/div[2]/div[2]/marketing/nz-layout/nz-layout/distribution-promotion/div/distribution-rule-management/distribution-rule-setting/rule-setting/nz-spin/div[2]/form/div[1]/div/p[2]/span[2]/div/nz-input/input')
    loc3=('xpath','//*[@id="container"]/div[2]/div[2]/div[2]/marketing/nz-layout/nz-layout/distribution-promotion/div/distribution-rule-management/distribution-rule-setting/rule-setting/nz-spin/div[2]/form/div[1]/div/p[3]/span[2]/div/nz-input/input')
    #优惠部分产生佣金开关
    loc4=('xpath','//*[@id="container"]/div[2]/div[2]/div[2]/marketing/nz-layout/nz-layout/distribution-promotion/div/distribution-rule-management/distribution-rule-setting/rule-setting/nz-spin/div[2]/form/div[1]/div/p[4]/span[2]/div/nz-switch/span')
    #当面付订单产生佣金
    loc5=('xpath','//*[@id="container"]/div[2]/div[2]/div[2]/marketing/nz-layout/nz-layout/distribution-promotion/div/distribution-rule-management/distribution-rule-setting/rule-setting/nz-spin/div[2]/form/div[1]/div/p[5]/span[2]/div/nz-switch/span')
    #申请电话
    loc6=('xpath','//*[@id="container"]/div[2]/div[2]/div[2]/marketing/nz-layout/nz-layout/distribution-promotion/div/distribution-rule-management/distribution-rule-setting/rule-setting/nz-spin/div[2]/form/div[2]/div/p[5]/span[2]/div/nz-input/input')
    #上下级关系锁定时间
    loc7=('xpath','//*[@id="container"]/div[2]/div[2]/div[2]/marketing/nz-layout/nz-layout/distribution-promotion/div/distribution-rule-management/distribution-rule-setting/rule-setting/nz-spin/div[2]/form/div[3]/div/p/span[2]/div/nz-input/input')
    #每月可提现次数
    loc8=('xpath','//*[@id="container"]/div[2]/div[2]/div[2]/marketing/nz-layout/nz-layout/distribution-promotion/div/distribution-rule-management/distribution-rule-setting/rule-setting/nz-spin/div[2]/form/div[4]/div/p[1]/span[3]/div/nz-input/input')
    #最低提现金额
    loc9=('xpath','//*[@id="container"]/div[2]/div[2]/div[2]/marketing/nz-layout/nz-layout/distribution-promotion/div/distribution-rule-management/distribution-rule-setting/rule-setting/nz-spin/div[2]/form/div[4]/div/p[2]/span[3]/div/nz-input/input')
    #保存
    loc10=('xpath','//*[@id="container"]/div[2]/div[2]/div[2]/marketing/nz-layout/nz-layout/distribution-promotion/div/distribution-rule-management/distribution-rule-setting/div/button')
    #保存后弹窗提示
    loc11=('xpath','/html/body/nz-confirm/div/div[2]/div[1]/div/div/div/div[1]/div/div')
    #页面装修弹窗
    loc12=('xpath','/html/body/app/jisu-sider/div/nz-spin/div[2]/ul/li[4]/div[2]/span')
    #保存后弹窗按钮
    loc13=('xpath','/html/body/nz-confirm/div/div[2]/div[1]/div/div/div/div[2]/button')
    def  distributionRule(self,first_Commission,second_Commission):
        '''分销规则设置'''
        url = "http://www.zhichiwangluo.com/management/marketing/distribution/distribution-rule-management/distribution-rule-management-rule?id=EQBYDcBill"

        self.driver.get(url)
        if self.isDispalyed(self.loc12)==True:
            self.click(self.loc12)
        self.click(self.loc1)
        self.clear(self.loc2)
        self.sendKyes(self.loc2,first_Commission)
        self.clear(self.loc3)
        self.sendKyes(self.loc3, second_Commission)
        if self.isSelected(self.loc4)== False:
            self.click(self.loc4)
        if self.isSelected(self.loc5) == False:
            self.click(self.loc5)
        self.clear(self.loc6)
        self.sendKyes(self.loc6,15100000000)
        self.clear(self.loc7)
        self.sendKyes(self.loc7, 10)
        self.clear(self.loc8)
        self.sendKyes(self.loc8, 3)
        self.clear(self.loc9)
        self.sendKyes(self.loc9, 10)
        self.click(self.loc10)

    def is_distrition_rule_sucess(self,_text):
        '''是否添加成功'''
        result=self.is_text_in_element(self.loc11, _text)
        print(result)
        self.click(self.loc13)
        return result




if __name__ == '__main__':
    driver=webdriver.Chrome()
    lg=LoginSuccess(driver)
    lg.login()
    d=Distribuiton(driver)
    d.distributionRule(30,20)
    _text="设置保存成功"
    result=d.is_distrition_rule_sucess(_text)
    print(result)




