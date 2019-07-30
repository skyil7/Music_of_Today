from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)#User 를 Foreign Key로
    date = timezone.localtime()
    likes = models.ManyToManyField(User, related_name='likes', blank=True)
    content = models.TextField()
    music = models.TextField()

    def likesCnt(self):
        if self.likes.count():
            return self.likes.count()
        return 0

    def createdDate(self):
        return self.date.date()

    def __str__(self):
        return self.title

