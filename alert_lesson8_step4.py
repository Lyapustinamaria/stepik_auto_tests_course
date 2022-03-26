from selenium import webdriver

try:
	browser = webdriver.Chrome()
	browser.execute_script("document.title='Script executing';alert('Robots at work');")
finally:
	time.sleep(5)
	browser.quit()