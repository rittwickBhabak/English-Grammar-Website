from django.urls import path
from grammar import views 

app_name = 'grammar'

urlpatterns = [
    path('books/', views.books, name='books'),
    path('book/1', views.book, name='book'),
    path('chapters/', views.chapters, name='chapters'),
    path('chapter/x', views.chapter, name='chapter'),
]