from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
browser.get(link)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
  button = browser.find_element_by_xpath("//button[@type='submit']")
  button.click()

  confirm = browser.switch_to.alert
  confirm.accept()

  xValue = browser.find_element_by_xpath("//span[@id='input_value']")
  x = xValue.text
  mathFunction = calc(x)

  input = browser.find_element_by_xpath("//input[@id='answer']")
  input.send_keys(mathFunction)

  submitButton = browser.find_element_by_xpath("//button[@type='submit']")
  submitButton.click()

finally:
    time.sleep(10)
    browser.quit()
