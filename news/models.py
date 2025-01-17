from django.utils import timezone
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth.models import User


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=News.status.Published)

class Category(models.Model):
    name = models.CharField(max_length=150)
    def __str__(self):
        return self.name


class News(models.Model):
    class Status(models.TextChoices):
        Draft = 'DF', 'Draft'
        Published = 'PB', 'Published'

    title = models.CharField(max_length=150)
    slug = models.TextField(max_length=350)
    body = models.TextField()
    image = models.ImageField(upload_to='news_photo/images',blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    publish_time = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.Draft)
    class Meta:
        ordering = ['-publish_time']

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('single', args=[self.title])
    objects = models.Manager()
    published = PublishedManager()
class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name

class Comentary(models.Model):
    news = models.ForeignKey(News,
                             on_delete=models.CASCADE,
                             related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created']
        # ordering = ['created'] # Birinchi yozilgan cament birinchi chiqadi

    def __str__(self):
        return f"Comment - {self.body} by {self.user}"
