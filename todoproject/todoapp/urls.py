
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<int:taskid>/', views.delete, name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    path('listviews/', views.ToDoListview.as_view(), name='listviews'),
    path('detailviews/<int:pk>/', views.ToDetailview.as_view(), name='detailviews'),
    path('updateview/<int:pk>/', views.TaskUpdateview.as_view(), name='updateview'),
    path('deleteview/<int:pk>/', views.TaskDeleteview.as_view(), name='deleteview'),
]
