from django.db import models
from django.utils.text import slugify

# Create your models here.


class About(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    slug = models.SlugField(unique=True, blank=True, null=True)
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(About, self).save(*args, **kwargs)
