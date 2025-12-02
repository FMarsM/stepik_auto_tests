from selenium import webdriver
from selenium.webdriver.common.by import By
import time


import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)
button = browser.find_element(By.TAG_NAME, "button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
x_el = browser.find_element(By.ID, "input_value")
browser.execute_script("return arguments[0].scrollIntoView(true);", x_el)
x = x_el.text
answer = calc(x)
ans = browser.find_element(By.ID, "answer")
ans.send_keys(answer)
chk = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
browser.execute_script("return arguments[0].scrollIntoView(true);", chk)
chk.click()
rb = browser.find_element(By.CSS_SELECTOR, '[for="robotsRule"]')
browser.execute_script("return arguments[0].scrollIntoView(true);", rb)
rb.click()
button.click()
time.sleep(15)