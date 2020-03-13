#coding:utf-8
import unittest
from common import HTMLTestRunner_cn
#运行所有的用例
casePath="D:\\github1\\untitled\\case"  #456用例路径66123
rule="test*.py" #匹配test开头,py结尾的文件
discover = unittest.defaultTestLoader.discover(start_dir=casePath ,pattern=rule)
print(discover)

#执行
reportPath ="D:\\github1\\untitled\\report"+"\\result.html" #报告要存放的路径
fp = open(reportPath,"wb")# open函数读取， wb以二进制写入
runner = HTMLTestRunner_cn.HTMLTestRunner(stream=fp,
                                          title="u即速应用自动化测试报告，测试结果如下：",
                                          description="用例执行情况")
runner.run(discover)

fp.close()#关闭
