from django.urls import path
from app import views
urlpatterns = [ 
    path('',views.index),
    # path('',views.method),
    path('guess',views.guess),
    # path('',views.greater),
    path('attempts',views.attempts),
    path('destroy',views.destroy)
]
