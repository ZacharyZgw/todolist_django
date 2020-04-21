from django.test import TestCase
from todo.models import Todo
from django.utils import timezone
# Create your tests here.

class WebUrlTest(TestCase):
    def test_indexPage(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code,200)
        response = self.client.get("/todo/list/")
        self.assertEqual(response.status_code, 200)
    def test_addPage(self):
        response = self.client.get("/todo/add")
        self.assertEqual(response.status_code, 301)
    def test_delete(self):
        todo = Todo(id=1,content="test delete url",pubTime=timezone.now())
        todo.save()
        response = self.client.get("/todo/delete/1")
        self.assertEqual(response.status_code, 301)
    def test_update(self):
        response = self.client.get("/todo/edit/")
        self.assertEqual(response.status_code, 301)