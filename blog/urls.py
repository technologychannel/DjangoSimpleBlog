from . import views
from django.urls import path

urlpatterns = [
    path('',views.index,name='homepage'),
    path('post/<int:postid>',views.single,name='single'),
]