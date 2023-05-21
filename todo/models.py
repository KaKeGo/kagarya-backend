from django.db import models
from django.utils import timezone

# Create your models here.


class ToDo(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    complited = models.BooleanField(default=False)
    date_created = models.DateTimeField(default=timezone.now())
    slug = models.SlugField(unique=True)
    
    def __str__(self):
        return self.title
    
