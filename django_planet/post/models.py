from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Article(models.Model):
    article_id = models.PositiveIntegerField(primary_key=True)
    article_type = models.CharField(max_length = 200 ,null=False)
    article_type_id = models.IntegerField(null=False)
    article_content = models.CharField(max_length=250,null=False)
    article_rank = models.IntegerField()
    user = models.ForeignKey(User)


class Comment(models.Model):
    comment_id = models.PositiveIntegerField(primary_key=True)
    comment_content = models.CharField(max_length=250, null=False)
    comment_rank = models.IntegerField()
    article_id = models.ForeignKey(Article)
    user = models.ForeignKey(User)
