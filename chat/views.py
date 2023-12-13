from django.shortcuts import render

# Create your views here.
def Job(request):
    return render(request,'pages/index.html')

def Chatting(request,group_name):
    print(group_name)
    return render(request,'pages/Chatpage.html',{'groupname': group_name})