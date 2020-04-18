from selenium import webdriver
import time


link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
browser.get(link)

try:

    input1 = browser.find_element_by_xpath("/html/body/div/form/div/input[1]")
    input1.send_keys("mathFunction")

    input2 = browser.find_element_by_xpath("/html/body/div/form/div/input[2]")
    input2.send_keys("mathFunction")

    input3 = browser.find_element_by_xpath("/html/body/div/form/div/input[3]")
    input3.send_keys("mathFunction")

    import os
    element = browser.find_element_by_xpath("//*[@id='file']")
    with open('test1.txt', 'w') as file:
        file.write('test1 for mls 228')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'test1.txt')
    element.send_keys(file_path)

    submitButton = browser.find_element_by_xpath("//button[@type='submit']")
    submitButton.click()

finally:
    time.sleep(10)
    browser.quit()

