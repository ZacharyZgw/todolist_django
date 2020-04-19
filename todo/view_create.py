from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from .models import Todo
@csrf_exempt
def create(request):
    if request.is_ajax():
        print('request_body',request.body)
        print('request_post',request.POST)
        content = request.POST.get('content','')
        pubTime = timezone.now()
        if content and pubTime:
            if content in [todo.content for todo in Todo.objects.all()]:
                error = '已创建{},请勿重复创建'.format(content)
                return JsonResponse({'status':10001,'message':error})
            else:
                Todo.objects.create(content=content,pubTime=pubTime)
                return JsonResponse({'status':10002,'message':'成功创建新的todo任务'})


