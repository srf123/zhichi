#condin:utf-8
from selenium import webdriver
import win32gui
import win32con
import time
from common import base
class Win32(base.Base):
    def __init__(self,driver):
        self.driver = driver

    def win32(self,locator):
        self.driver.get('file:///C:/Users/Administrator/Desktop/fileupload.html')
        locator.click()
        time.sleep(1)

        # win32gui
        dialog = win32gui.FindWindow('#32770', '文件上传')  # 对话框。窗口类名和窗口名。在窗口查找工具：WinSpy可以找到
        ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)
        '''搜索类名和窗体名匹配的窗体，并返回这个窗体的句柄。不区分大小写，找不到就返回0。
         参数：
              hwndParent：若不为0，则搜索句柄为hwndParent窗体的子窗体。
              hwndChildAfter：若不为0，则按照z-index的顺序从hwndChildAfter向后开始搜索子窗体，否则从第一个子窗体开始搜索。
              lpClassName：字符型，是窗体的类名，这个可以在Spy++里找到。
              lpWindowName：字符型，是窗口名，也就是标题栏上你能看见的那个标题。'''
        ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)
        Edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None)  # 上面三句依次寻找对象，直到找到输入框Edit对象的句柄
        button = win32gui.FindWindowEx(dialog, 0, 'Button', None)  # 确定按钮Button
        win32gui.SendMessage(Edit, win32con.WM_SETTEXT, None, 'd:\\all_money.wmv')  # 往输入框输入绝对地址
        win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 按button
        print (locator.get_attribute('value'))
       # self.dr.quit()
if __name__ == '__main__':
    driver=webdriver.Chrome()
    win=Win32(driver)
    loctor=('xpath','//*[@id="file2"]')
    base.Base().findElement(loctor)
    win.win32()