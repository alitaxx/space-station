#ecshop后台登录
#夺宝奇兵添加
#启动浏览器
from selenium import webdriver
from selenium.webdriver.common.by import By


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
#进入frame
driver.switch_to.frame('menu-frame')
time.sleep(1)
driver.find_element(By.XPATH,'//ul[@id="menu-ul"]/li[2]').click()
driver.find_element(By.LINK_TEXT,'夺宝奇兵').click()
time.sleep(1)
#退出frame
driver.switch_to.parent_frame()
driver.switch_to.frame('main-frame')
#添加夺宝奇兵
driver.find_element(By.LINK_TEXT,'添加夺宝奇兵').click()
driver.find_element(By.NAME,'snatch_name').send_keys("718购物节")
driver.find_element(By.NAME,'keywords').send_keys("玉泽")
driver.find_element(By.CSS_SELECTOR,'[type=button]').click()
#添加时间
js = "document.getElementById('start_time_id').removeAttribute('readonly')"
driver.execute_script(js)
driver.find_element(By.ID,'start_time_id').clear()
driver.find_element(By.ID,'start_time_id').send_keys('2020-07-20 12:46')

js = "document.getElementById('end_time_id').removeAttribute('readonly')"
driver.execute_script(js)
driver.find_element(By.ID,'end_time_id').clear()
driver.find_element(By.ID,'end_time_id').send_keys('2020-07-30 12:46')

#输入价格
driver.find_element(By.NAME,'start_price').clear()
driver.find_element(By.NAME,'start_price').send_keys('50')
driver.find_element(By.NAME,'end_price').clear()
driver.find_element(By.NAME,'end_price').send_keys('180')
driver.find_element(By.NAME,'max_price').clear()
driver.find_element(By.NAME,'max_price').send_keys('10')
#活动描述
driver.find_element(By.NAME,'desc').send_keys("五一七天乐，天天乐翻车")
driver.find_element(By.CSS_SELECTOR,'[type=submit]').click()
time.sleep(1)
driver.find_element(By.XPATH,'/html').click()
#返回列表、查看
driver.find_element(By.LINK_TEXT,'返回活动列表').click()
time.sleep(2)
driver.find_element(By.XPATH,'//div[@id="listDiv"]/table/tbody/tr[2]/td[8]/a[1]/img').click()
time.sleep(1)
driver.find_element(By.LINK_TEXT,'夺宝奇兵').click()
time.sleep(1)
#编辑夺宝奇兵
driver.find_element(By.XPATH,'//div[@id="listDiv"]/table/tbody/tr[2]/td[8]/a[2]/img').click()
driver.find_element(By.NAME,'snatch_name').clear()
driver.find_element(By.NAME,'snatch_name').send_keys('720购物节，来就送宝马')
#开始结束时间
js = "document.getElementById('start_time_id').removeAttribute('readonly')"
driver.execute_script(js)
driver.find_element(By.ID,'start_time_id').clear()
driver.find_element(By.ID,'start_time_id').send_keys('2020-07-21 12:12')

js = "document.getElementById('end_time_id').removeAttribute('readonly')"
driver.execute_script(js)
driver.find_element(By.ID,'end_time_id').clear()
driver.find_element(By.ID,'end_time_id').send_keys('2020-08-01 12:12')

driver.find_element(By.NAME,'start_price').clear()
driver.find_element(By.NAME,'start_price').send_keys('80')
driver.find_element(By.NAME,'end_price').clear()
driver.find_element(By.NAME,'end_price').send_keys('718')
driver.find_element(By.NAME,'max_price').clear()
driver.find_element(By.NAME,'max_price').send_keys('66')
driver.find_element(By.NAME,'cost_points').clear()
driver.find_element(By.NAME,'cost_points').send_keys('12')
driver.find_element(By.NAME,'desc').clear()
driver.find_element(By.NAME,'desc').send_keys("五一七天乐，天天乐翻车，我们不放假")
driver.find_element(By.CSS_SELECTOR,'[type=submit]').click()
driver.find_element(By.LINK_TEXT,'返回活动列表').click()
time.sleep(2)
#删除
driver.find_element(By.XPATH,'//div[@id="listDiv"]/table/tbody/tr[2]/td[8]/a[3]/img').click()
time.sleep(1)
driver.switch_to.alert.accept()
time.sleep(1)
#关闭并退出
driver.quit()