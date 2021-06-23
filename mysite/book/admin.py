from django.contrib import admin
from .models import Book, Question

# Register your models here.
admin.site.register(Book)
admin.site.register(Question)