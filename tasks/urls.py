from django.urls import path
from .views import *

urlpatterns = [
    path('dashboard/', dashboard, name='home'),
    # path('update/<int:pk>/', dashboard, name='task_update'),
    path('update/<str:slug>/', update_task.as_view(), name='update'),
    path('complete/<int:pk>/', mark_task_completed.as_view(), name='completed'),
    path('delete/<int:pk>/', delete_task, name='delete' ),
]