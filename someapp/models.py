from django.db import models

# Create your models here.

class Comments(models.Model):
    username=models.CharField(max_length=50,default="Anonymous")
    content=models.TextField()

    def __str__(self):
        return self.username