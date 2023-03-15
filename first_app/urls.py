from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name="index"), #atilsamancioglu.com/first_app/
    path("<str:item>/",views.course, name="course"), #atilsamancioglu.com/first_app/python
    path("<int:num1>/<int:num2>/",views.multiply_view,name="multiply"), #atilsamancioglu.com/first_app/5/4
    
]