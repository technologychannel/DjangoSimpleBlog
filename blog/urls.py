from . import views
from django.urls import path

urlpatterns = [
    path('',views.index,name='homepage'),
    path('post/',views.single,name='single'),
]