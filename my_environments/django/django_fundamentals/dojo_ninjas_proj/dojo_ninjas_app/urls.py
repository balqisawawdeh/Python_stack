from django.urls import path
from . import views
urlpatterns = [ 
    path('', views.index),
    path('add',views.create_dojo),
    path('addninja',views.addninjas),   
    path('displayalldojos',views.getalldojo),
    path('displayallninjas',views.getallninjas)
]
