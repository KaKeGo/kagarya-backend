import string
import random

from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.utils.text import slugify
from django.urls import reverse

from users.models import User

# Create your models here.

User = get_user_model()

TODO_CATEGORY = [
    ('', ''),
    ('Django', 'Django'),
    ('React', 'React'),
]

def random_slug():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(15))

class TodoPlan(models.Model):
    name = models.CharField(max_length=30)
    todo = models.ManyToManyField('Todo', blank=True, null=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, null=True, blank=True, max_length=255)
    
    def __str__(self):
        return f'{self.name}'
    
    def author_name(self):
        return self.author.username
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(random_slug() + '+/+' + self.name)
        super(TodoPlan, self).save(*args, **kwargs)

class Todo(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    category = models.CharField(max_length=50, choices=TODO_CATEGORY, default='')
    tasks = models.ManyToManyField('Task', blank=True, null=True)
    completed = models.BooleanField(default=False)
    date_created = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(random_slug() + '+/+' + self.title)
        super(Todo, self).save(*args, **kwargs)

class Task(models.Model):
    name = models.CharField(max_length=30)
    complited = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.name} / {self.complited}'
