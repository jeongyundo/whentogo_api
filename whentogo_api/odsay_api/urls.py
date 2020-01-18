from django.urls import path
from odsay_api import views

urlpatterns = [
    path('getGpsdata/', views.getGpsdata),
]