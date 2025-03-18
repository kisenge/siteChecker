from django.urls import path
from . import views


urlpatterns = [
    path('submit-ur/',views.startBackgroundTask),
    path('getData/<int:taskID>',views.getData),
]