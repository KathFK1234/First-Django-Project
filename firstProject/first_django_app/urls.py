from django.urls import path
from . import views

# Defining a list that contains all the addresses and their associated views
urlpatterns = [
    path('function', views.function_based_view), # This path directs user view to the function-based view
    path('class', views.class_based_view.as_view()), # This path directs user to the class-based view
]