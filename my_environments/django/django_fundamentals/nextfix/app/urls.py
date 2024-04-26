from django.urls import path
from . import views
urlpatterns = [ 
    path('', views.index),
    path('register', views.register),
    path('shows', views.validate_login),
    path('shows/<int:show_id>', views.details),
    path('shows/new', views.new_show),
    path('shows/edit/<int:show_id>', views.edit_show),
]
