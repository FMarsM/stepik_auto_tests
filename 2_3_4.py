from selenium import webdriver
from selenium.webdriver.common.by import By
import time


import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
browser = webdriver.Chrome()
link = "http://suninjuly.github.io/alert_accept.html"
browser.get(link)
button = browser.find_element(By.TAG_NAME, "button")
button.click()
sure = browser.switch_to.alert
sure.accept()
x_el = browser.find_element(By.ID, "input_value")
ans = browser.find_element(By.ID, "answer")
x = x_el.text
answer = calc(x)
ans.send_keys(answer)
btn = browser.find_element(By.CSS_SELECTOR, "button")
btn.click()
time.sleep(15)