from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"

def sum(x, y):
  return str(x + y)

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element_by_id("num1").text
    x_int = int(x)
    y = browser.find_element_by_id("num2").text
    y_int = int(y)
    answer = sum(x_int, y_int)

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_visible_text(answer)
    button = browser.find_element_by_css_selector(".btn.btn-default").click()

finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()