from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseNotFound


course_dictionary = {
    "python" : "Python Course Page",
    "java" : "Java Course Page",
    "kotlin" : "Kotlin Course Page",
    "swift" : "Swift Course Page"
    }

def index(request):
    return HttpResponse("This is first Django project, first index")

def course(request, item):
    try:
        course = course_dictionary[item]
        return HttpResponse(course)
    except:
        return HttpResponseNotFound("Not found! Please look for another course!")
        #raise Http404("Not found! Please look for another course!")
    #return HttpResponse(course_dictionary.get(item,"Not found!"))

def multiply_view(request, num1, num2):
    return HttpResponse(f"{num1} * {num2} = {num1 * num2}")
