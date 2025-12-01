from django.urls import path
from . import views

urlpatterns = [
    path('', views.root_url_view),
    path('function', views.function_based_view),
    path('class', views.class_based_view.as_view())
]