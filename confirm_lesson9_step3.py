from selenium import webdriver
import time
import math

link = 'http://suninjuly.github.io/alert_accept.html'

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

try:
	browser = webdriver.Chrome()
	browser.get(link)

	button1 = browser.find_element_by_css_selector('.btn.btn-primary').click()
	confirm = browser.switch_to.alert
	confirm.accept()

	x_element = browser.find_element_by_id("input_value")
	x = x_element.text
	y = calc(x)
	input1 = browser.find_element_by_id('answer').send_keys(y)
	button2 = browser.find_element_by_css_selector('.btn.btn-primary').click()
finally:
	time.sleep(10)
	browser.quit()