from selenium import webdriver
import time
import os

link = 'http://suninjuly.github.io/file_input.html'

try:
	browser = webdriver.Chrome()
	browser.get(link)

	input1 = browser.find_element_by_name("firstname").send_keys("Mary")
	input2 = browser.find_element_by_name("lastname").send_keys("Yram")
	input3 = browser.find_element_by_name("email").send_keys("maryyram@gmail.com")

	current_dir = os.path.abspath(os.path.dirname(__file__))
	file_path = os.path.join(current_dir, 'testFile.txt')
	input4 = browser.find_element_by_id("file").send_keys(file_path)

	button = browser.find_element_by_css_selector(".btn.btn-primary").click()
finally:
	time.sleep(10)
	browser.quit()