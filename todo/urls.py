from django.urls import path

from .views import (
    TodoPlanView,
    TodoDetailPlanView,
    TodoPlanCreateView,
 
    TodoDetailView,
    TodoCreateView,
    
    TaskDetailView,
    TaskCreateView,
)

app_name = 'todo'


urlpatterns = [
    path('plan/', TodoPlanView.as_view(), name='plan'),
    path('plan/create/', TodoPlanCreateView.as_view(), name='plan_create'),
    path('create/', TodoCreateView.as_view(), name='plan_create'),
    path('task/create/', TaskCreateView.as_view(), name='plan_create'),
    
    
    path('plan/<slug>/', TodoDetailPlanView.as_view(), name='plan_detail'),
    
    path('<slug>/', TodoDetailView.as_view(), name='todo_detail'),
    
    path('task/<name>/', TaskDetailView.as_view(), name='task_detail'),
]
