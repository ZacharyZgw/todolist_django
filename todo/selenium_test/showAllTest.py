import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
class TestSelectAll(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
    def test_queryAll(self):
        '''
        测试是否正确渲染所有代办事项
        :return:
        '''
        driver = self.driver
        driver.get('http://127.0.0.1:8000/todo/list')
        todolist = driver.find_elements_by_tag_name('li')
        assert len(todolist)==4
    def tearDown(self):
        time.sleep(10)
        self.driver.close()