from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
browser.get(link)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
  time.sleep(1)
  button = browser.find_element_by_xpath("//button[@type='submit']")
  button.click()



  print(browser.window_handles)
  new_window = browser.window_handles[1]
  browser.switch_to.window(new_window)


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
