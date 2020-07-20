'''
添加广告语
'''
#后台登录
#启动浏览器
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
import time
driver.maximize_window()
driver.implicitly_wait(20)
#打开浏览器
driver.get("http://192.168.1.38/upload/admin/privilege.php?act=login")
# time.sleep(1)
# #输入账号密码登录
driver.find_element(By.NAME,'username').send_keys('alita')
driver.find_element(By.NAME,'password').clear()
driver.find_element(By.NAME,'password').send_keys('dami131441')
driver.find_element(By.CSS_SELECTOR,'[type=submit]').click()
time.sleep(1)
#进入fram
driver.switch_to.frame('menu-frame')
driver.find_element(By.XPATH,'//ul[@id="menu-ul"]/li[4]').click()
driver.find_element(By.LINK_TEXT,'广告列表').click()
#跳出并进入另一个frame
driver.switch_to.parent_frame()
driver.switch_to.frame('main-frame')
driver.find_element(By.LINK_TEXT,'添加广告').click()
#添加广告
driver.find_element(By.NAME,'ad_name').send_keys('奥迪R5')
locator = driver.find_element(By.NAME,'media_type')
select = Select(locator)
select.select_by_value('0')

locator = driver.find_element(By.NAME,'position_id')
select = Select(locator)
select.select_by_value('159')
#设置时间
js = "document.getElementById('start_time').removeAttribute('readonly')"
driver.execute_script(js)
driver.find_element(By.NAME,'start_time').send_keys('2020-07-19')

js = "document.getElementById('end_time').removeAttribute('readonly')"
driver.execute_script(js)
driver.find_element(By.NAME,'end_time').send_keys('2020-08-19')
driver.find_element(By.NAME,'ad_img').send_keys('E:\\u=656760854,293154485&fm=26&gp=0.jpg')
driver.find_element(By.CSS_SELECTOR,'[type=submit]').click()
driver.find_element(By.LINK_TEXT,'返回广告列表').click()
time.sleep(3)
driver.find_element(By.XPATH,'//div[@id="listDiv"]/table/tbody/tr[2]/td[8]/span/a[2]/img').click()
time.sleep(1)
driver.switch_to.alert.accept()

time.sleep(2)
driver.quit()