from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
browser.get(link)

try:
 num1 = browser.find_element_by_xpath("//span[@id='num1']").text
 num2 = browser.find_element_by_xpath("//span[@id='num2']").text
 nomer1 = int(num1)
 nomer2 = int(num2)

 summa = nomer1 + nomer2
 a = str(summa)
 print (a)

 select = Select(browser.find_element_by_tag_name("select"))
 select.select_by_value(a)

 submit = browser.find_element_by_xpath("/html/body/div/form/button")
 submit.click()

finally:
    time.sleep(5)
    browser.quit()

