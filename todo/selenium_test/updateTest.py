import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
class TestCreate(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
    def testupdate(self):
        driver = self.driver
        driver.get('http://127.0.0.1:8000/todo/list')
        driver.find_element_by_id("19@编写新建todo代码").click()
        time.sleep(1)
        driver.find_element_by_id("edit_content").clear()
        time.sleep(1)
        driver.find_element_by_id("edit_content").send_keys("编写新建todo的测试代码")
        driver.find_element_by_id("submit_content").click()
        time.sleep(1)
        obj = driver.find_element_by_id("19@编写新建todo的测试代码")
        assert obj != None
    def tearDown(self):
        time.sleep(10)
        self.driver.close()