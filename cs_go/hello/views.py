from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def index(request):
    return render(request,"hello/hello.html")

def greet(request,name):
    return render(request,"hello/hello.html",context={"name":name})

