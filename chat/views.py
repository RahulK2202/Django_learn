from django.shortcuts import render

# Create your views here.
def Job(request):
    return render(request,'pages/index.html')

def Chatting(request):
    return render(request,'pages/Chatpage.html')