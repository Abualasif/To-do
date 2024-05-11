from django.urls import path
from .views import index, task_list, task_detail, sign_up, log_in, dashboard, log_out

urlpatterns = [
    path('', index, name='index'),
    path('sign_up', sign_up, name='sign_up'),
    path('log_in', log_in, name='log_in'),
    path('log_out', log_out, name='log_out'),
    path('dashboard', dashboard, name='dashboard'),
    path('task_list', task_list, name='task_list'),
    path('<int:pk>', task_detail, name='task_detail'),
]