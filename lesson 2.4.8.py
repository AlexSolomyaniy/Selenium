from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
browser.get(link)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:

  button = WebDriverWait(browser,12).until(
      EC.text_to_be_present_in_element((By.ID, "price"), "$100")
  )
  button1 = browser.find_element_by_xpath("//*[@id='book']").click()


  xValue = browser.find_element_by_xpath("//span[@id='input_value']")
  x = xValue.text
  mathFunction = calc(x)

  input = browser.find_element_by_xpath("//input[@id='answer']")
  input.send_keys(mathFunction)

  submitButton = browser.find_element_by_xpath("//button[@type='submit']")
  submitButton.click()

finally:
    time.sleep(12)
    browser.quit()
