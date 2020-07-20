#ecshop前台登录购物车管理删除、清空购物车
#启动浏览器
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)
#打开浏览器
driver.get("http://192.168.1.38/upload")
time.sleep(1)
#鼠标悬浮
locator = driver.find_element(By.XPATH,'//div[@id="HandleLI2_3"]/a')
action = ActionChains(driver)
action.move_to_element(locator).perform()
driver.find_element(By.LINK_TEXT,'单反相机').click()
driver.find_element(By.LINK_TEXT,'索尼').click()
time.sleep(1)
js = "document.getElementById('number').value='666'"
driver.execute_script(js)
time.sleep(1)
driver.find_element(By.XPATH,'//form[@id="ECS_FORMBUY"]/ul[3]/li[2]/a/img').click()
time.sleep(2)
#继续购物
driver.find_element(By.XPATH,'/html/body/div[7]/div[1]/table/tbody/tr/td[1]/a/img').click()
time.sleep(1)
locator1 = driver.find_element(By.XPATH,'//div[@id="HandleLI2_1"]/a')
action = ActionChains(driver)
action.move_to_element(locator1).perform()
driver.find_element(By.XPATH,'//dd[@id="DisSub2_1"]/a[5]').click()
time.sleep(1)
driver.find_element(By.LINK_TEXT,'紫色衣服').click()
driver.find_element(By.XPATH,'//form[@id="ECS_FORMBUY"]/ul[3]/li[2]/a/img').click()

# 删除购物车删除商品
driver.find_element(By.XPATH,'//form[@id="formCart"]/table[1]/tbody/tr[2]/td[7]/a').click()
time.sleep(1)
driver.switch_to.alert.accept()
time.sleep(1)
#清空购物车
driver.find_element(By.CLASS_NAME,'bnt_blue_1').click()
time.sleep(3)
#关闭退出
driver.quit()