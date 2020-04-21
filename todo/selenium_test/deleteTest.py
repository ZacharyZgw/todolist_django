import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
class TestSelectAll(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
    def testDelete(self):
        driver = self.driver
        driver.get('http://127.0.0.1:8000/todo/list')
        old_todolist_len = len(driver.find_elements_by_tag_name('li'))
        time.sleep(1)
        driver.find_element_by_id("19").click()
        time.sleep(1)
        new_todolist_len = len(driver.find_elements_by_tag_name('li'))
        assert new_todolist_len == old_todolist_len-1
    def tearDown(self):
        time.sleep(10)
        self.driver.close()