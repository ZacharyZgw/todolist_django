from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Todo
@csrf_exempt
def update(request):
    if request.is_ajax():
        print('request_body', request.body)
        print('request_post', request.POST)
        id = request.POST.get('id','')
        content = request.POST.get('content', '')
        try:
            Todo.objects.filter(id=int(id)).update(content=content)
            return JsonResponse({'status': 10005, 'message': "更新成功"})
        except:
            return JsonResponse({'status': 10006, 'message': "更新失败"})