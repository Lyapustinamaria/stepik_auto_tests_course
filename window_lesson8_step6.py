from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/redirect_accept.html"

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

try:
	browser = webdriver.Chrome()
	browser.get(link)

	button1 = browser.find_element_by_css_selector(".trollface.btn.btn-primary").click()

	second_window_name = browser.window_handles[1]
	browser.switch_to.window(second_window_name)

	x_element = browser.find_element_by_id("input_value").text
	x = calc(x_element)

	input1 = browser.find_element_by_id("answer").send_keys(x)
	button2 = browser.find_element_by_css_selector(".btn.btn-primary").click()
finally:
	time.sleep(10)
	browser.quit()