from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='list'),
    path('new/', views.PostCreate.as_view(), name='create'),
    path('read/<int:pk>', views.PostRead.as_view(), name='read'),
    path('update/<int:pk>', views.PostUpdate.as_view(), name='update'),
    path('delete/<int:pk>', views.PostDelete.as_view(), name='delete'),
]