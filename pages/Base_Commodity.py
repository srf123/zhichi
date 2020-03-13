#coding:utf-8
from selenium import webdriver
from common.base import Base
import time
from pages.login import LoginSuccess

class Commodity(Base):
    '''添加电商商品'''

    #定位登录
    loc1 = ("id", "login-username")
    loc2 = ("css selector", "[id=login-password]")
    loc3 = ("xpath", "//*[@id='login-btn']")
    #添加商品
    #点击商品管理
    loc6= ('xpath','//*[@id="container"]/e-commerce/div[2]/div[1]/inline-sider/nz-spin/div[2]/div/div/div/div[3]')
    #添加商品按钮
    loc7=("xpath",'//*[@id="container"]/e-commerce/div[2]/div[2]/goods/nz-layout'
                  '/nz-content/goods-list/nz-layout/div/div[2]/div[1]/button[1]')
    #商品名称
    loc8=("xpath",'//*[@id="container"]/e-commerce/div[2]/div[2]/goods-operation'
                  '/nz-content/div/div[2]/div[1]/div[2]/div[2]/input')
    #添加商品主图
    loc9=("xpath",'//*[@id="container"]/e-commerce/div[2]/div[2]'
                  '/goods-operation/nz-content/div/div[2]/div[1]/div[5]/div[2]/div')
    #选择图片
    loc10=("xpath",'/html/body/app/photo-modal/div/nz-modal[1]/div/div[2]/div[1]'
                   '/div/div[2]/div[2]/nz-spin/div[2]/div/div/div[1]/img')
    #点击不裁剪
    loc11=("xpath",'/html/body/app/photo-modal/photo-crop-modal/nz-modal'
                   '/div/div[2]/div[1]/div/div[3]/div/button[1]')
    #价格
    locl2 = ("xpath",'//*[@id="container"]/e-commerce/div[2]/div[2]/'
                     'goods-operation/nz-content/div/div[2]/div[1]/div[10]/div[2]/input')
    #库存
    loc13=("xpath",'//*[@id="container"]/e-commerce/div[2]/div[2]/'
                   'goods-operation/nz-content/div/div[2]/div[1]/div[11]/div[2]/input')
    #iframe
    loc14 = ("id","ueditor_0")

    #商品描述
    loc15 = ("xpath","/html/body")
    #快递
    loc16 = ("xpath",'//*[@id="container"]/e-commerce/div[2]/div[2]'
                     '/goods-operation/nz-content/div/div[2]/div[1]/div[16]/div[2]/label[1]')
    #确定
    loc17 = ("xpath",'//*[@id="container"]/e-commerce/div[2]/div[2]/'
                     'goods-operation/nz-content/div/div[2]/div[6]/div/button[1]')
    #商品名
    loc18 = ("xpath",'//*[@id="container"]/e-commerce/div[2]/div[2]/goods/nz-layout'
                     '/nz-content/goods-list/nz-layout/nz-layout/nz-content/table-items'
                     '/nz-layout/nz-content/nz-table/div/nz-spin/div[2]/div/div/div/div/div/table/thead/tr/th[4]')
    #新增的列表
    loc19 = ("xpath",'//*[@id="container"]/e-commerce/div[2]/div[2]/goods/nz-layout/'
                     'nz-content/goods-list/nz-layout/nz-layout/nz-content/table-items/nz-layout/'
                     'nz-content/nz-table/div/nz-spin/div[2]/div/div/div/div/div/table/tbody/tr[1]/td[4]/div/span')



    #添加商品
    def add_commodity(self,com="自动添加商品"):
        self.driver.get("http://www.zhichiwangluo.com/management/shops/e-commerce/goods/goods-list?id=EQBYDcBill")
        self.click(self.loc6)
        self.click(self.loc7)
        self.sendKyes(self.loc8,com)
        self.click(self.loc9)
        self.click(self.loc10)
        self.click(self.loc11)
        #使操作使元素在当前页面可见
        self.driver.execute_script("arguments[0].scrollIntoView()",self.findElement(self.loc9))
        time.sleep(3)
        #self.click(self.locl2)
        self.sendKyes(self.locl2,1)
        self.sendKyes(self.loc13, 100)

        # js方法切换到iframe，不需要在退出
        js = 'document.getElementById("ueditor_0").contentWindow.document.body.innerHTML="商品描述"'
        self.driver.execute_script(js)

        #切换到iframe
        #self.iframe(self.loc14)
        self.sendKyes(self.loc15,"商品描述")
        # 退出iframe
        # self.driver.switch_to.default_content()


        self.driver.execute_script("arguments[0].scrollIntoView()", self.findElement(self.loc16))
        time.sleep(3)

        #选择快递
        if self.isSelected(self.loc16) == False:
            self.click(self.loc16)
        self.click(self.loc17)
     #判断商品是否添加成功
    def is_addComm_successful(self,_text):
        return self.is_text_in_element(self.loc19,_text)#判断



if __name__ == '__main__':
    driver=webdriver.Chrome()
    commo = Commodity(driver)

    a =LoginSuccess(driver)
    a.login()


    comm = "自动添加商品"+time.strftime("%Y_%m_%d_%H_%M_%S")
    commo.add_commodity(comm)
    result = commo.is_addComm_successful(comm)
    print(result)
    commo.is_addComm_successful(result)





