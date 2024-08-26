
from django.contrib import admin
from django.urls import path,re_path
from todoApp.views import TaskView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('view/', TaskView.as_view(), name='task-list-or-detail'),
    path('view/<uuid:pk>/', TaskView.as_view(), name='task-detail'),
]
