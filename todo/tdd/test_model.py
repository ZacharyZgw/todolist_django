from django.test import TestCase
from todo.models import Todo
from django.utils import timezone
# Create your tests here.
#测试模型文件
class EntryModelTest(TestCase):

    def test_string_representation(self):
        todo = Todo(content="first testcase",pubTime=timezone.now())
        self.assertEqual(str(todo),todo.content) #false,需要将模型用字符串表示，添加__str__方法
