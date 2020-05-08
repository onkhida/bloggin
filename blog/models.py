from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from ckeditor.fields import RichTextField
import uuid

class Post(models.Model):
    title = models.CharField(max_length=80)
    thumbnail = models.ImageField(upload_to='post_thumbnails', default='picture.png')
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    content = RichTextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    draft = models.BooleanField(default=True)

    class Meta:
        ordering = ('-publish',)

    def __unicode__(self):
        return self.id

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.id])
