from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('addtwo',views.addtwo),
    path('reset',views.reset)	
]
