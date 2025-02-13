from django.urls import path
from . import views


urlpatterns = [
    path('post/',views.postData),
    path('get/',views.getData),
]