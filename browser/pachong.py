import time
from selenium import webdriver
from selenium.webdriver.common.by import By  # 与下面的2个都是等待时要用到
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from pathlib import Path
from pathlib import Path
import os
print (os.getcwd())
path = Path(os.getcwd())
path = Path(str(path.parent.absolute()) + '/create_truth_table/verilog.txt')
f = open(path,"r")
veri = f.read()
url = 'http://v1.cellocad.org'
driver = webdriver.Chrome()
driver.get(url)
wait = WebDriverWait(driver, 25)
driver.maximize_window()  # 窗口最大化
user = wait.until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="login_username"]')))
user.send_keys('cyx5226') # 用户名
pw = wait.until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="login_password"]')))
pw.send_keys('1234') #登陆密码
print('login param input success')

login = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="btnLogin"]')))  # 登录按钮
login.click()
print('login success')
time.sleep(10)


design_name = driver.find_element_by_xpath('//*[@id="design_name"]')
design_name.send_keys('design3') # design name

verilog = driver.find_element_by_xpath('//*[@id="verilogAreaDiv"]/div[1]')
driver.execute_script("arguments[0].CodeMirror.setValue(arguments[1]);",verilog, veri)

input_clear1 = driver.find_element_by_xpath('//*[@id="input_output_div"]/button[1]')
input_clear1.click()

input_dropdown = driver.find_element_by_xpath('//*[@id="input_pulldown"]')
input_dropdown.click()