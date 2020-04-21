import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
class TestCreate(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
    def testcreate(self):
        driver = self.driver
        driver.get('http://127.0.0.1:8000/todo/list')
        input_box = driver.find_element_by_id("todo_content")
        old_todolist_len = len(driver.find_elements_by_tag_name('li'))
        input_box.send_keys("创建Selenium自动化测试")
        time.sleep(1)
        input_box.send_keys(Keys.ENTER)
        time.sleep(1)
        new_todolist_len = len(driver.find_elements_by_tag_name('li'))
        assert new_todolist_len == old_todolist_len+1
    def tearDown(self):
        time.sleep(10)
        self.driver.close()