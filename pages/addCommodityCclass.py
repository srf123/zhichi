#conding:utf-8

from common.base import Base
from pages.login import LoginSuccess as lg
import time
from selenium import webdriver

class AddCommClass(Base):
    '''添加电商分类'''


    #商品管理
    loc1=('xpath','//*[@id="container"]/e-commerce/div[2]/div[1]/inline-sider/nz-spin/div[2]/div/div/div/div[3]')
    #分类管理
    loc2=('xpath','//*[@id="container"]/e-commerce/div[2]/div[2]'
                  '/goods/nz-layout/nz-content/goods-list/nz-layout/div/div[2]/div[2]/button')
    #新增分类
    loc3=('xpath','//*[@id="container"]/e-commerce/div[2]/div[2]/type-list/nz-layout/nz-header/span[1]/button')
    #分类名称
    loc4=('xpath','//*[@id="name"]/input')
    #添加分类图标
    loc5=('xpath','//*[@id="container"]/e-commerce/div[2]/div[2]'
                  '/shops-add-type/nz-layout/nz-content/form/div[3]/div[2]/div')
    #选择图片
    loc6=('xpath','/html/body/app/photo-modal/div/nz-modal[1]/div/div[2]/div[1]'
                  '/div/div[2]/div[2]/nz-spin/div[2]/div/div/div[1]/img')
    #点击不裁剪
    loc7=('xpath','/html/body/app/photo-modal/photo-crop-modal/nz-modal/div/div[2]/div[1]/div/div[3]/div/button[1]')
    #点击保存
    loc8=('xpath','//*[@id="container"]/e-commerce/div[2]/div[2]/shops-add-type/nz-layout/nz-content/div/button[1]')
    # 分页下标ul
    loc11 = ('xpath', '//*[@id="container"]/e-commerce/div[2]/div[2]/type-list/nz-layout'
                  '/nz-layout/nz-content/nz-table/div/nz-spin/div[2]/nz-pagination/ul')
    # 获取分类表格
    loc12 = ('xpath', '//*[@id="container"]/e-commerce/div[2]/div[2]/type-list/nz-layout/nz-layout'
                      '/nz-content/nz-table/div/nz-spin/div[2]/div/div/div/div/div/table/tbody')



    def addcommclass(self,fl):
        self.driver.get('http://www.zhichiwangluo.com/management/shops/e-commerce/goods/goods-list')
        time.sleep(3)
        self.click(self.loc1)
        self.click(self.loc2)
        self.click(self.loc3)
        self.sendKyes(self.loc4,fl)
        self.click(self.loc5)
        time.sleep(2)
        self.click(self.loc6)
        self.click(self.loc7)
        self.click(self.loc8)
        time.sleep(2)

        #获取最后一页的下标
        lilen =self.lastpages(self.loc11)
        # 跳转到最后一页
        self.loc9 = ('xpath', '//*[@id="container"]/e-commerce/div[2]/div[2]/type-list/nz-layout/nz-layout'
                         '/nz-content/nz-table/div/nz-spin/div[2]/nz-pagination/ul/li[' + lilen + ']')
        self.click(self.loc9)


        # 获取table最后一行的下标中（每新增一行最后一行的下标都会变化）
        lrlen= self.lasttable(self.loc12)
        # 获取分类名称
        self.loc10 = ('xpath', '//*[@id="container"]/e-commerce/div[2]/div[2]/type-list/nz-layout/nz-layout/nz-content'
                          '/nz-table/div/nz-spin/div[2]/div/div/div/div/div/table/tbody/tr[' + lrlen + ']/td[2]')

    #判断是否添加成功
    def is_addcommclass_sucess(self,_text):
        result=self.is_text_in_element(self.loc10, _text)
        print(result)
        return result


if __name__ == '__main__':
    driver = webdriver.Chrome()
    ac=AddCommClass(driver)

    lg(driver).login()
    com='电商分类'+time.strftime('%Y_%m_%d_%H_%M_%S')
    ac.addcommclass(com)
    result = ac.is_addcommclass_sucess(com)
    print(result)















