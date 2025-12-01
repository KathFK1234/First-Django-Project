from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.
# Make sure to link the views to addresses, ie, URL mapping, at the app and project levels
# Function-based view:
def function_based_view(request):
    return HttpResponse("Hello World! Created the first function-based view!")

# Class-based view:
class class_based_view(View):
    def get(self, request):
        return HttpResponse("Hello you! Created the first class-based view!")

def root_url_view(request):
    return HttpResponse("Hello you! This is the root or home page!")
