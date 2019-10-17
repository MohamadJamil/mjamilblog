from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import unittest

class SearchBox_TestCase(unittest.TestCase):
    def test_000_no_result(slef):
        browser = webdriver.Chrome()
        browser.get("https://www.python.org")
        assert "Python" in browser.title
        search_box = browser.find_element_by_name("q")
        search_box.clear()
        search_box.send_keys("qwfdawfqwgfqwfq")
        search_box.send_keys(Keys.RETURN)
        assert "No results found."  in browser.page_source
    def test_001_no_result(slef):
        browser = webdriver.Chrome()
        browser.get("https://www.python.org")
        assert "Python" in browser.title
        search_box = browser.find_element_by_name("q")
        search_box.clear()
        search_box.send_keys("pycon")
        search_box.send_keys(Keys.RETURN)
        assert "No results found." not in browser.page_source

if __name__ == '__main__':
    print("this is unit testing for example_unittest.py")#only runs from here wont run from test_everything.py
    unittest.main(verbosity=2)

# browser = None
#
# try:
#     browser = webdriver.Chrome()
#     browser.get("https://www.python.org")
#     assert "Python" in browser.title
#     search_box = browser.find_element_by_name("q")
#     search_box.clear()
#     search_box.send_keys("pycon")
#     search_box.send_keys(Keys.RETURN)
#     assert "No results found." not in browser.page_source
#     print("test passed")
#     sleep(15)
# finally:
#     if browser:
#         browser.close()
