from django.urls import path
from . import views
#
#Url paths are found in order to trigger the function on views.py
urlpatterns = [
    path('', views.home),
    path('products/', views.products),
    path('customer/', views.customer),
]