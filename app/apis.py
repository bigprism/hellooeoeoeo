from django.http import JsonResponse

from .models import Task



def task_list_api(request):
    tasks = Task.objects.all()
    data = []
    for task in tasks:
        data.append({
            'id': task.id,
            'title': task.title,
            'description': task.description,
            'status': task.status,
            'priority': task.priority,
            'created_at': task.created_at,
            'updated_at': task.updated_at,
        })
    return JsonResponse(data, safe=False)



def task_detail_api(request, pk):
    task = Task.objects.get(pk=pk)
    data = {
        'id': task.id,
        'title': task.title,
        'description': task.description,
        'status': task.status,
        'priority': task.priority,
        'created_at': task.created_at,
        'updated_at': task.updated_at,
    }
    return JsonResponse(data)



def task_create_api(request):
    if request.method == 'POST':
        data = request.POST.dict()
        task = Task.objects.create(**data)
        data = {
            'id': task.id,
            'title': task.title,
            'description': task.description,
            'status': task.status,
            'priority': task.priority,
            'created_at': task.created_at,
            'updated_at': task.updated_at,
        }
        return JsonResponse(data)
    return JsonResponse({'error': 'Bad request'}, status=400)



def task_update_api(request, pk):
    if request.method == 'PUT':
        data = request.PUT.dict()
        task = Task.objects.get(pk=pk)
        task.title = data['title']
        task.description = data['description']
        task.status = data['status']
        task.priority = data['priority']
        task.save()
        data = {
            'id': task.id,
            'title': task.title,
            'description': task.description,
            'status': task.status,
            'priority': task.priority,
            'created_at': task.created_at,
            'updated_at': task.updated_at,
        }
        return JsonResponse(data)
    return JsonResponse({'error': 'Bad request'}, status=400)



def task_delete_api(request, pk):
    if request.method == 'DELETE':
        task = Task.objects.get(pk=pk)
        task.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'error': 'Bad request'}, status=400)