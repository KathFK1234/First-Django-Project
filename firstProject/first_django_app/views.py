from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views import View

# Create your views here.
# Make sure to link the views to addresses, ie, URL mapping
# Function-based view:
def hello_world(request):
    return HttpResponse("Hello World!")

# Class-based view:
class first_classb_view():
    def get(self, request):
        return HttpResponse("Created the first class-based view!")
