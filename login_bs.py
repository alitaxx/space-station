#ecshop后台登录
#启动浏览器
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
import time
driver.maximize_window()
driver.implicitly_wait(20)
#打开浏览器
driver.get("http://localhost/upload/admin/privilege.php?act=login")
# time.sleep(1)
# #输入账号密码登录
driver.find_element(By.NAME,'username').send_keys('alita')
driver.find_element(By.NAME,'password').clear()
driver.find_element(By.NAME,'password').send_keys('dami131441')
driver.find_element(By.CSS_SELECTOR,'[type=submit]').click()
time.sleep(1)

# driver.quit()