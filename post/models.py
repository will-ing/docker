from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
class Posts(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    isbn = models.CharField(max_length=13)
    released = models.CharField(max_length=20)

    def __str__(self):
        return self.title
