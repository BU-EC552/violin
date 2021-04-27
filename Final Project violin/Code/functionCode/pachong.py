import time
from selenium import webdriver
from selenium.webdriver.common.by import By  # 与下面的2个都是等待时要用到
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from pathlib import Path
import os


def main(username, password, name, list1, list2, ucf_file_source, showwiring):

    url = 'http://v1.cellocad.org'
    driver = webdriver.Chrome('C:/Users/12524/Documents/GitHub/violin/browser/chromedriver.exe')
    driver.get(url)
    wait = WebDriverWait(driver, 25)
    driver.maximize_window()  # 窗口最大化

    def signin(username, password):
        user = wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="login_username"]'))) 
        user.send_keys(username) # 用户名
        pw = wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="login_password"]')))
        pw.send_keys(password) #登陆密码
        print('login param input success')

    signin(username, password)

    login = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="btnLogin"]')))  # 登录按钮
    login.click()
    print('login success')
    time.sleep(10) 

    def set_design_name(name):
        design_name = driver.find_element_by_xpath('//*[@id="design_name"]') 
        design_name.send_keys(name) # design name

    # set_design_name(name)

    def write_verilog():
        print(os.getcwd())
        path = Path(os.getcwd())
        path = Path(str(path.parent.absolute()) + '/violin/functions/verilog.txt')
        f = open(path,"r")
        veri = f.read()
        verilog = driver.find_element_by_xpath('//*[@id="verilogAreaDiv"]/div[1]')
        driver.execute_script("arguments[0].CodeMirror.setValue(arguments[1]);",verilog, veri)
    write_verilog()
    input_clear1 = driver.find_element_by_xpath('//*[@id="input_output_div"]/button[1]')
    input_clear1.click()

    time.sleep(10)
    #output_clear = driver.find_element_by_xpath('//*[@id="input_output_div"]/button[2]]')
    #output_clear.click()

    #input_dropdown = driver.find_element_by_xpath('//*[@id="input_pulldown"]')
    #input_dropdown.click()
    #print("successfully dropdown input")

    input_select = Select(driver.find_element_by_id('input_pulldown'))
    output_select = Select(driver.find_element_by_id('output_pulldown'))


    def input_output_select(list1,list2):
        len1 = len(list1)
        len2 = len(list2)
        i = 0
        j = 0
        while i < len1:
            input_select.select_by_value(list1[i])
            i += 1
        while j < len2:
            output_select.select_by_value(list2[j])
            j += 1

    input_output_select(list1, list2)


    def upload_ucf(ucf_file_source):
        Options_page = driver.find_element_by_xpath('//*[@id="options_link"]')
        Options_page.click()

        ucf = driver.find_element_by_xpath('//*[@id="upload_verilog"]')
        ucf.send_keys(ucf_file_source)

    if ucf_file_source !='':
        upload_ucf("test.UCF.json")

    def show_wiring():
        Results_page = driver.find_element_by_xpath('//*[@id="results_link"]')
        Results_page.click()
        wiring = driver.find_element_by_xpath('//*[@id="r2"]')
        wiring.click()

    if showwiring == "show_wiring":
        show_wiring()


    time.sleep(5)
    verilog_page = driver.find_element_by_xpath('//*[@id="verilog_link"]')
    verilog_page.click()
    time.sleep(5)
    set_design_name(name)
    Run = driver.find_element_by_xpath('//*[@id="submit"]')
    Run.click()
    time.sleep(100)