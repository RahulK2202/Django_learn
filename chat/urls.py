from django.urls import path,include
from .import views

urlpatterns = [

    # path('',views.Job,name='job'),
    path('<str:group_name>/',views.Chatting,name='chatting'),

]