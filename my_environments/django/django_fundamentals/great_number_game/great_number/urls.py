from django.urls import path, include           # import include

urlpatterns = [
    path('', include('app.urls'))
    ]
