from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Person(User):
    age=models.IntegerField(default=20)
    user_type=models.CharField(default='viewer',max_length=10)
    reputation=models.IntegerField(default=0)

    def __str__(self):
        return self.email

class Article(models.Model):
    name=models.CharField(max_length=50)
    content=models.TextField()
    author=models.ForeignKey(Person,on_delete=models.SET(None))

class Fact(models.Model):
    written_in=models.ForeignKey(Article,on_delete=models.CASCADE)
    text=models.TextField()

class FactReview(models.Model):
    fact=models.ForeignKey(Fact,on_delete=models.CASCADE)
    reviewd_by=models.ForeignKey(User,on_delete=models.SET(None))
    comment=models.TextField()
    vote=models.IntegerField(default=0)

class ArticleReview(models.Model):
    article=models.ForeignKey(Article,on_delete=models.CASCADE)
    reviewd_by = models.ForeignKey(User, on_delete=models.SET(None))
    comment = models.TextField()
    vote = models.IntegerField(default=0)

class ThirdPartyArticleReview(models.Model):
    url=models.URLField()
    reviewd_by = models.ForeignKey(User, on_delete=models.SET(None))
    comment = models.TextField()
    vote = models.IntegerField(default=0)



