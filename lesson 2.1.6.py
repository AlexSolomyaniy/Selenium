from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
browser.get(link)



def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:

    xImg = browser.find_element_by_xpath("//img[@id='treasure']")
    xValue = xImg.get_attribute("valuex")
    print (xValue)
    x=xValue
    mathFunction = calc(x)

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

