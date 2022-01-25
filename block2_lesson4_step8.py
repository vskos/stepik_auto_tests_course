from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
button = browser.find_element_by_css_selector("button#book")
WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element ((By.ID, 'price'), '$100'))

button.click()

x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(x)

answer_field = browser.find_element_by_id("answer")
answer_field.send_keys(y)

button_submit = browser.find_element_by_css_selector("button[type='submit']")
button_submit.click()

time.sleep(10)
# ожидание чтобы визуально оценить результаты прохождения скрипта
# закрываем браузер после всех манипуляций
browser.quit()
