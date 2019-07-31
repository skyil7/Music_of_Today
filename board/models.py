from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import re

class Post(models.Model):
    title = models.CharField(max_length=100)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)#User 를 Foreign Key로
    date = timezone.localtime()
    likes = models.ManyToManyField(User, related_name='likes', blank=True)
    content = models.TextField()
    music = models.TextField()
    tag_set = models.ManyToManyField('Tag', related_name='tag', blank=True)

    def likesCnt(self):
        if self.likes.count():
            return self.likes.count()
        return 0

    def createdDate(self):
        return self.date.date()

    def __str__(self):
        return self.title

    def tag_save(self):
        self.tag_set.clear()
        tags = re.findall(r'#(\w+)\b', self.content)

        if not tags:
            return

        for t in tags:
            tag, tag_created = Tag.objects.get_or_create(name=t)
            self.tag_set.add(tag)  # ManyToManyField 에 인스턴스 추가

class Tag(models.Model):
    name=models.CharField(max_length=80, unique=True)
    def __str__(self):
        return self.name