from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import os

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"
browser.get(link)
l = open("file.txt", "w")
current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла
element = browser.find_element(By.ID, 'file')
element.send_keys(file_path)
frst = browser.find_element(By.CSS_SELECTOR, '[name="firstname"]')
frst.send_keys("John")
scnd = browser.find_element(By.CSS_SELECTOR, '[name="lastname"]')
scnd.send_keys("Doe")
mail = browser.find_element(By.CSS_SELECTOR, '[name="email"]')
mail.send_keys("test@te.st")
btn = browser.find_element(By.TAG_NAME, 'button')
btn.click()

time.sleep(10)
