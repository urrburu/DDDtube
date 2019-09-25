from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.shortcuts import reverse
import re
import pyperclip
class Tag(models.Model):
    name = models.CharField(max_length=140, unique=True)

    def __str__(self):
        return self.name

class clip(models.Model):
    clipID = models.CharField(max_length = 300)
    contents = models.CharField(max_length = 500,  null=True)
    tag_set = models.ManyToManyField('Tag', blank=True)
    updated = models.DateTimeField(auto_now=True)
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    author = models.ForeignKey(User,on_delete=models.CASCADE, related_name='user_clip')
    title = models.CharField(max_length=200)
    streamer = models.CharField(max_length=10)
    url = models.CharField(max_length=500,default="no url")
    embed_url = models.CharField(max_length=1000, default="no embed")


    class Meta:
        ordering = ['-updated']
    def __str__(self):
        return self.author.username+" "+self.updated.strftime("%Y-%m-%d %H:%M:%S")
    def get_absolute_url(self):
        return reverse('clip:clip_detail', args=[str(self.id)])

    def tag_save(self):
        tags = re.findall(r'#(\w+)\b', self.contents)

        if not tags:
            return

        for t in tags:
            tag, tag_created = Tag.objects.get_or_create(name=t)
            self.tag_set.add(tag)  # NOTE: ManyToManyField 에 인스턴스 추가

    #def copy_url(self):
    #    pyperclip.copy(self.url)

    #def copy_iframe(self):
    #    pyperclip.copy(self.embed_url)

# Create your models here
