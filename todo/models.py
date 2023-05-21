from django.db import models
from django.utils import timezone
from django.utils.text import slugify

# Create your models here.


class ToDo(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    complited = models.BooleanField(default=False)
    date_created = models.DateTimeField(default=timezone.now())
    slug = models.SlugField(unique=True, null=True, blank=True)
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(ToDo, self).save(*args, **kwargs)
