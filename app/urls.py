from django.urls import path

from . import views

urlpatterns = [
    path('task_list/', views.task_list, name='task_list'),
    path('task_detail/<int:pk>/', views.task_detail, name='task_detail'),
    path('task_create/', views.task_create, name='task_create'),
    path('task_update/<int:pk>/', views.task_update, name='task_update'),
    path('task_delete/<int:pk>/', views.task_delete, name='task_delete'),

    path('task_list_api/', views.task_list_api, name='task_list_api'),
    path('task_detail_api/<int:pk>/', views.task_detail_api, name='task_detail_api'),
    path('task_create_api/', views.task_create_api, name='task_create_api'),
    path('task_update_api/<int:pk>/', views.task_update_api, name='task_update_api'),
    path('task_delete_api/<int:pk>/', views.task_delete_api, name='task_delete_api'),
]