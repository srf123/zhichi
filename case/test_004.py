from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from common.base import Base

driver = webdriver.Chrome()
driver.get("http://www.zhichiwangluo.com/index.php?r=login/Ulogin")
# #title_is断言（预期结果）（driver）,当前页面的title是否完全等于（==）预期字符串
# r = EC.title_is("登录")(driver)
# print(r)
# assert r
#
# #title_contains 当前页面的title是否包含预期结果

loc=("id","login-btn")
Ba=Base(driver)
r1=Ba.is_title("登录")
r2=Ba.title_contains("登")
r=Ba.is_text_in_element(loc,"登录123")
print(r)
print(r1)
print(r2)
Ba.move_to_element(loc)