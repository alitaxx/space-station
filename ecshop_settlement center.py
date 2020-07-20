#ecshop前台登录购物车购物流程-结算中心
#启动浏览器
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
import time
driver.maximize_window()
driver.implicitly_wait(20)
#打开浏览器
driver.get("http://192.168.1.38/upload/index.php")
# time.sleep(2)
#登录账号
driver.find_element(By.XPATH,'//font[@id="ECS_MEMBERZONE"]/a[1]').click()
# time.sleep(2)
driver.find_element(By.CLASS_NAME,"inputBg").send_keys("alitax")
driver.find_element(By.NAME,'password').send_keys("dami131441")
driver.find_element(By.NAME,'submit').click()
time.sleep(1)
#查看购物车
driver.find_element(By.LINK_TEXT,'查看购物车').click()
#继续购物
driver.find_element(By.XPATH,'/html/body/div[7]/div[1]/table/tbody/tr/td[1]/a/img').click()
time.sleep(1)

#鼠标悬浮选择
locator = driver.find_element(By.XPATH,'//div[@id="HandleLI2_1"]/a')
action = ActionChains(driver)
action.move_to_element(locator).perform()
driver.find_element(By.XPATH,'//dd[@id="DisSub2_1"]/a[5]').click()
time.sleep(1)
#购买衣服添加到购物车并结算
driver.find_element(By.CLASS_NAME,'goodsimg').click()
driver.find_element(By.XPATH,'//form[@id="ECS_FORMBUY"]/ul[3]/li[2]/a/img').click()
driver.find_element(By.XPATH,'/html/body/div[7]/div[1]/table/tbody/tr/td[2]/a/img').click()
driver.find_element(By.CSS_SELECTOR,'[type=image]').click()
time.sleep(3)


#关闭并退出浏览器
driver.quit()