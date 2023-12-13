from django.urls import path,include
from .import views

urlpatterns = [

    # path('',views.Job,name='job'),
    path('',views.Chatting,name='chatting'),

]