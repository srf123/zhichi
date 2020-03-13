#coding:utf-8
from common.base import Base
from selenium import webdriver
from pages.login import LoginSuccess
import time

from selenium.webdriver.common.action_chains import ActionChains
class UserManage_(Base):
    '''用户管理'''
    # 页面装修弹窗
    loc1 = ('xpath', '/html/body/app/jisu-sider/div/nz-spin/div[2]/ul/li[4]/div[2]/span')
    #选中第一个用户
    loc2=('xpath','//*[@id="container"]/div/div/div/users/div/div[2]/div[2]/table-items/nz-table/div/nz-spin/div[2]/div/div/div/div/div/table'
                  '/tbody/tr[1]/td[1]/label/span/input')
    #点击更多
    loc3=("xpath",'//*[@id="container"]/div/div/div/users/div/div[2]/div[2]/table-items/div/nz-dropdown[2]/div/button')


    # 减扣储值金
    loc4= ('xpath', '//*[@id="cdk-overlay-3"]/div/div/ul/li[5]')
    #输入减扣金额
    loc5=('xpath','//*[@id="container"]/div/div/div/users/div/div[2]/div[2]/table-items/top-up-dialog/nz-modal/div'
                 '/div[2]/div[1]/div/div[2]/div[1]/div/input')
    #备注信息
    loc6=("xpath",'//*[@id="container"]/div/div/div/users/div/div[2]/div[2]/table-items/top-up-dialog'
                    '/nz-modal/div/div[2]/div[1]/div/div[2]/div[2]/div/textarea')
    #点击确定
    loc7=('xpath','//*[@id="container"]/div/div/div/users/div/div[2]/div[2]/table-items/top-up-dialog/nz-modal/div'
                 '/div[2]/div[1]/div/div[3]/button[2]')
    # 充值储值金
    loc8 = ('xpath', '//*[@id="cdk-overlay-3"]/div/div/ul/li[4]/span')
    # 输入储值金额
    loc9 =('xpath','.//*[@id="container"]/div/div/div/users/div/div[2]/div[2]/table-items/top-up-dialog/nz-modal'
                   '/div/div[2]/div[1]/div/div[2]/div[1]/div/input')
    # 弹窗确定
    loc10= ('xpath', '//*[@id="container"]/users/nz-content/div/div[2]/div[2]/table-items/top-up-dialog/nz-modal'
                     '/div/div[2]/div[1]/div/div[3]/button[2]')

    # 赠送积分
    loc11= ('xpath', '//*[@id="cdk-overlay-3"]/div/div/ul/li[6]/span')
    #积分赠送数量
    loc12=('xpath','//*[@id="container"]/div/div/div/users/div/div[2]/div[2]/table-items/user-integral-dialog/nz-modal'
             '/div/div[2]/div[1]/div/div[2]/div/div/nz-input-number/div[2]/input')
    #点击确定
    loc13=('xpath','.//*[@id="container"]/div/div/div/users/div/div[2]/div[2]/table-items/user-integral-dialog[1]'
                   '/nz-modal/div/div[2]/div[1]/div/div[3]/button[2]')


    #积分减扣
    loc14= ('xpath','//*[@id="cdk-overlay-3"]/div/div/ul/li[7]/span')
    #积分减扣数量
    loc15=('xpath', '//*[@id="container"]/div/div/div/users/div/div[2]/div[2]/table-items/user-integral-dialog/nz-modal' 
    '/div/div[2]/div[1]/div/div[2]/div/div[1]/nz-input-number/div[2]/input')
    #点击确定
    loc16=('xpath','//*[@id="container"]/div/div/div/users/div/div[2]/div[2]/table-items/user-integral-dialog/nz-modal'
                   '/div/div[2]/div[1]/div/div[3]/button[2]')

    # 赠送会员卡
    loc17= ('xpath', '//*[@id="cdk-overlay-3"]/div/div/ul/li[8]')
    #点击确定
    loc18=('xpath','//*[@id="container"]/div/div/div/users/div/div[2]/div[2]/table-items/give-vip-dialog/nz-modal'
                 '/div/div[2]/div[1]/div/div[3]/button[2]')
    # 赠送优惠券
    loc19= ('xpath', '//*[@id="cdk-overlay-3"]/div/div/ul/li[9]')
    #点击确定
    loc20=('xpath','//*[@id="container"]/div/div/div/users/div/div[2]/div[2]/table-items/give-coupon-dialog/nz-modal'
                 '/div/div[2]/div[1]/div/div[3]/button[2]')
    #用户列表页面第一个用户的现有储值金额
    loc21=('xpath','//*[@id="container"]/div/div/div/users/div/div[2]/div[2]/table-items/nz-table/div/nz-spin/div[2]'
                   '/div/div/div/div/div/table/tbody/tr[1]/td[4]')

    # 用户列表页面第一个用户的现有积分
    loc22=('xpath','//*[@id="container"]/div/div/div/users/div/div[2]/div[2]/table-items/nz-table/div/nz-spin/div[2]'
                   '/div/div/div/div/div/table/tbody/tr[1]/td[5]')
    #赠送的会员卡名称
    loc23=('xpath','//*[@id="container"]/div/div/div/users/div/div[2]/div[2]/table-items/give-vip-dialog/nz-modal/div'
                   '/div[2]/div[1]/div/div[2]/div/nz-select/div/div/div[2]')
    #赠送后用户列表中的会员卡名称
    loc24=('xpath','//*[@id="container"]/div/div/div/users/div/div[2]/div[2]/table-items/nz-table/div/nz-spin/div[2]'
                   '/div/div/div/div/div/table/tbody/tr[1]/td[8]')
    #赠送前的优惠券数量

    loc25=("xpath",'//*[@id="container"]/div/div/div/users/div/div[2]/div[2]/table-items/nz-table/div/nz-spin/div[2]'
                   '/div/div/div/div/div/table/tbody/tr[1]/td[7]')
    #赠送的优惠券数量
    loc26=('xpath','//*[@id="container"]/div/div/div/users/div/div[2]/div[2]/table-items/give-coupon-dialog/nz-modal'
                   '/div/div[2]/div[1]/div/div[2]/div/div[2]/input')
    #积分弹窗确定
    loc27=('xpath','/html/body/nz-confirm/div/div[2]/div[1]/div/div/div/div[2]/button')




    def total_usermanage(self,loc):
        '''封装公共方法'''
        self.driver.get('http://www.zhichiwangluo.com/management/users?id=EQBYDcBill')
        self.click(self.loc1)
        # 获取赠送/减扣前的数据
        self.before_num= self.td_text(loc)
        print(self.before_num)
        print(type(self.before_num))
        self.click(self.loc2)
        self.click(self.loc3)
    def add_money(self):
        '''充值储值金'''
        self.total_usermanage(self.loc21)
        time.sleep(3)
        self.click(self.loc8)
        time.sleep(2)
        self.sendKyes(self.loc9,"1")
        print("=======================")
        time.sleep(2)
        self.click(self.loc10)
    def is_addMoneySucess(self):
        '''判断金额是否储值成功'''
        # 获取充值后现有金额
        self.after_money = float(self.td_text(self.loc21))
        print(self.after_money)
        if self.after_money ==float(self.before_num)+1:
            print("111111111")
            return True
        else:
            return False

    def reduce_money(self):
        '''减扣储值金'''
        self.total_usermanage(self.loc21)
        self.click(self.loc4)
        self.click(self.loc5)
        self.sendKyes(self.loc5, 1)
        self.sendKyes(self.loc6, "测试自动减扣")
        self.click(self.loc7)
    def is_reduceMoneySucess(self):
        '''判断储值金减扣是否成功'''
        #获取减扣后的储值金额
        after_money=float(self.td_text(self.loc21))
        if float(self.before_num)==after_money+1:
            print(True)
        else:
            print(False)

    def add_integral(self):
        '''赠送积分'''
        self.total_usermanage(self.loc22)
        if self.isEnabled(self.loc11)== False:
            self.click(self.loc2)
            self.click(self.loc3)
            self.click(self.loc11)
        else:
            self.click(self.loc11)

        self.sendKyes(self.loc12,1)
        self.que=self.findElement(self.loc13)
        print('111111111111')
        #ActionChains(self.driver).move_to_element(self.que).move_by_offset(5,5).click().perform()
        self.click(self.loc13)
        self.click(self.loc27)
        time.sleep(2)
        self.after_integral = int(self.td_text(self.loc22))


    def is_addIntegralSucess(self):
        '''判断积分是否赠送成功'''

        print(self.after_integral)
        print(self.before_num)
        if int(self.before_num) == self.after_integral-1:
            print('-------------------')
            return True
        else:
            return False

    def reduce_integral(self):
        '''减扣积分'''
        self.total_usermanage(self.loc22)
        self.click(self.loc14)
        self.sendKyes(self.loc15,1)
        time.sleep(2)
        self.click(self.loc16)

    def is_reduceIntegralSucess(self):
        '''判断积分减扣是否成功'''
        after_integral = int(self.td_text(self.loc22))
        if int(self.before_num) == after_integral+1:
            return True
        else:
            return False

    def give_Vipcard(self):
        '''赠送会员卡'''
        self.total_usermanage(self.loc24)
        self.click(self.loc17)
        self.click(self.loc18)

    def is_addVipSucess(self):
        '''会员卡是否赠送成功'''
        after_integral = self.td_text(self.loc23)
        if self.before_num == after_integral:
            return True
        else:
            return False

    def give_coupon(self):
        '''赠送优惠券'''
        self.total_usermanage(self.loc26)
        self.click(self.loc19)
        self.click(self.loc20)

    def is_giveCoupon(self):
        '''判断优惠券是否赠送成功'''
        after_coupon=int(self.td_text(self.loc25))#赠送后的数量
        num=int(self.td_text(self.loc26))#赠送的数量

        if int(self.before_num)==after_coupon-num:
            return True
        else:
            return False









if __name__ == '__main__':
    driver=webdriver.Chrome()
    lg=LoginSuccess(driver)
    lg.login()
    ug=UserManage_(driver)
    # ug.add_money()
    # ug.is_addMoneySucess()
    # ug.reduce_money()
    ug.add_integral()
    ug.is_addIntegralSucess()
    driver.close()



