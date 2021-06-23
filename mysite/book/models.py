from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=500)
    file = models.FileField(upload_to='documents/')
    last_read_page = models.IntegerField(default=1)
    zoom_level = models.FloatField(default=100.0)

    def __str__(self):
        return self.name 

class Question(models.Model):
    question = models.TextField()
    answer = models.TextField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    page_number = models.IntegerField()

    def __str__(self):
        return self.question

