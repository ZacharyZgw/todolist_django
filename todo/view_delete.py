from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Todo
@csrf_exempt
def delete(request,id):
    # if request.is_ajax():
    #     print('request_body', request.body)
    #     print('request_post', request.POST)
    #     id = request.P.get('todo_id','')
    #     try:
    #         Todo.objects.filter(id=int(id)).delete()
    #         return JsonResponse({'status':10003,'message':"删除成功"})
    #     except:
    #         return JsonResponse({'status':10004,'message':"删除失败"})
    try:
        Todo.objects.filter(id=int(id)).delete()
        return JsonResponse({'status': 10003, 'message': "删除成功"})
    except:
        return JsonResponse({'status': 10004, 'message': "删除失败"})

