from django.urls import path
from . import views

app_name = 'practice'

urlpatterns = [
    path('', views.home, name='home'),
    path('start-exam/', views.start_exam, name='start_exam'),
    path('evaluate-exam/', views.evaluate_exam, name='evaluate_exam'),
]