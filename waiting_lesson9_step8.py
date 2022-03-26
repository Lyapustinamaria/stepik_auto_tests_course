from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

link = "http://suninjuly.github.io/explicit_wait2.html"

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

try:
	browser = webdriver.Chrome()
	browser.implicitly_wait(5)
	browser.get(link)
	text1 = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
	button1 = browser.find_element_by_id("book").click()
	x_element = browser.find_element_by_id("input_value").text
	x = calc(x_element)

	input1 = browser.find_element_by_id("answer").send_keys(x)
	button2 = browser.find_element_by_id("solve").click()
finally:
	time.sleep(10)
	browser.quit()