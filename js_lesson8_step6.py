from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/execute_script.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("input_value")
    y = calc(x_element.text)

    input1 = browser.find_element_by_id("answer").send_keys(y)
    checkbox = browser.find_element_by_id("robotCheckbox").click()
    radiobutton = browser.find_element_by_id("robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", radiobutton)
    radiobutton.click()
    button = browser.find_element_by_css_selector(".btn.btn-primary")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()