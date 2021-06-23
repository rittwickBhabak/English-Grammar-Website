from django.urls import path
from book import views 

app_name = 'book'
urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('<int:book_id>/', views.book, name='book'),
    path('update-last-page/', views.update_last_page, name='update_last_page'),
    path('update-zoom-level/', views.update_zoom_level, name='update_zoom_level'),
    path('add-question/', views.add_question, name='add_question'),
    path('update-question/', views.update_question, name='update_question'),
]