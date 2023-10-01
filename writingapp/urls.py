from django.urls import path
from . import views

app_name = 'writingapp'

urlpatterns = [
    path('', views.home, name = 'home'),
    path('writing_area/', views.writing_area, name = 'writing_area'),
]
