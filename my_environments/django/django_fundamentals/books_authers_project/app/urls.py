from django.urls import path
from . import views
urlpatterns = [ 
    path('', views.index),
    path('books/<int:book_id>', views.view_book),
    path('add_auth_to_book/<int:book_id>',views.add_auth_to_book),
    path('create_book', views.create_book),
    path('remove', views.remove_book),
    path('authers', views.auther),
    path('create_auther', views.create_auther),
    path('remove_auther', views.remove_auther),
    path('authers/<int:auther_id>', views.view_auther),
]