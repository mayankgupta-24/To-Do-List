from django.urls import path
from . import views

urlpatterns=[
    path('', views.task_list, name='tasks'),
    path('add/', views.add_task, name='add'),
    path('update/<int:id>/', views.update_task, name='update'),
    path('delete/<int:id>/', views.delete_task, name='delete')
]