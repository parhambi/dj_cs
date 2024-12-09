from django.shortcuts import render

# Create your views here.
todos = [
    "create music",
    "make money",
    "learn django"
]
def index(request):
    return render(request,"tasks/index.html",{"todos":todos})