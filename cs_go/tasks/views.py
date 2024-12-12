from django.shortcuts import render,redirect
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
todos = [
    "create music",
    "make money",
    "learn django"
]
class NewTaskForm(forms.Form):
    task = forms.CharField(label="New task")
    priority = forms.IntegerField(label="priority",min_value=1,max_value=20)

def index(request):
    if  "todos" not in request.session:
        request.session["todos"] = []
    return render(request,"tasks/index.html",{"todos":request.session["todos"]})

def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["todos"] += [task]
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request,"add/index.html",{"task":form})
    context = {"task":NewTaskForm()}
    return render(request,"add/index.html",context)