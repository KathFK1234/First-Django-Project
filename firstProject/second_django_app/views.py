from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.
def function_based_view(request):
    return HttpResponse("This is the function-based view in the second app")

class class_based_view(View):
    def get(self, request):
        return HttpResponse("Hello! You reached the class-based view of the second app!")
    
def root_url_view(request):
    return HttpResponse("You have reached the root home page of the second app!")