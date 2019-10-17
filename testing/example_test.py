from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
browser = None

try:
    browser = webdriver.Chrome()
    browser.get("https://www.python.org")
    assert "Python" in browser.title
    search_box = browser.find_element_by_name("q")
    search_box.clear()
    search_box.send_keys("pycon")
    search_box.send_keys(Keys.RETURN)
    assert "No results found." not in browser.page_source
    print("test passed")
    sleep(15)
finally:
    if browser:
        browser.close()
