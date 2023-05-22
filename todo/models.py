import string
import random

from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.

TODO_CATEGORY = [
    ('', ''),
    ('Django', 'Django'),
    ('React', 'React'),
]


def random_slug():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(40))

class ToDo(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    category = models.CharField(max_length=30, choices=TODO_CATEGORY, default='')
    completed = models.BooleanField(default=False)
    date_created = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(unique=True, null=True, blank=True)
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(random_slug() + '-' + self.title)
        super(ToDo, self).save(*args, **kwargs)
        
    def get_absolute_url(self):
        return reverse("todo:detail", kwargs={"slug": self.slug})
    
    def get_todo_count(self):
        return ToDo.objects.count()
