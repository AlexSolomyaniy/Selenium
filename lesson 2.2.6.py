from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
browser.get(link)

import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:

    xValue = browser.find_element_by_xpath("//span[@id='input_value']")
    x=xValue.text
    mathFunction = calc(x)

    browser.execute_script("window.scrollBy(0, 100);")

    input = browser.find_element_by_xpath("//input[@id='answer']")
    input.send_keys(mathFunction)

    checkbox = browser.find_element_by_xpath("//input[@id='robotCheckbox']")
    checkbox.click()

    radiobutton = browser.find_element_by_xpath("//input[@id='robotsRule']")
    radiobutton.click()

    submitButton = browser.find_element_by_xpath("//button[@type='submit']")
    submitButton.click()

finally:
    time.sleep(10)
    browser.quit()

