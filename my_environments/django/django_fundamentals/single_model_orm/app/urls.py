from django.urls import path     
from . import views
urlpatterns = [ 
    path('', views.index),
    path('create', views.create),
    path('remove', views.remove)
]
