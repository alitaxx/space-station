#ecshop前台登录
#启动浏览器
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
import time
driver.maximize_window()
driver.implicitly_wait(20)
#打开浏览器
driver.get("http://localhost/upload/index.php")
# time.sleep(2)
#登录账号
driver.find_element(By.XPATH,'//font[@id="ECS_MEMBERZONE"]/a[1]').click()
# time.sleep(2)
driver.find_element(By.CLASS_NAME,"inputBg").send_keys("alitax")
driver.find_element(By.NAME,'password').send_keys("dami131441")
driver.find_element(By.NAME,'submit').click()
time.sleep(3)

#关闭并退出浏览器
driver.quit()