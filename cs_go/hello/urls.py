from . import views
from django.urls import path,include
app_name = "hello"
urlpatterns = [
    path("",views.index,name="index"),
    path("greet/<str:name>/",views.greet,name = "greet")


]