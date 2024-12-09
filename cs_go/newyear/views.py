from django.shortcuts import render
from datetime import datetime
# Create your views here.
def index(request):
    now = datetime.now()
    new_year = False
    if now.month == 1 and now.day ==1:
        new_year=True

    context = {"newyear":new_year}
    return render(request,"newyear/index.html",context)