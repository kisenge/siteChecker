from django.urls import path
from . import views


urlpatterns = [
    path('submit-ur/',views.startBackgroundTask),
    path('get/<int:taskID>',views.getData),
]