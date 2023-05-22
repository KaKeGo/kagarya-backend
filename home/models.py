from django.db import models

# Create your models here.

ACCESS_CHOICES = [
    ('Admin', 'Admin'),
    ('Authenticated user', 'Authenticated user'),
    ('Any', 'Any'),
]


class ShowApiUrl(models.Model):
    name = models.CharField(max_length=100)
    access  = models.CharField(max_length=20, choices=ACCESS_CHOICES, default='Admin')
    url = models.CharField(max_length=255, null=True, blank=True)
    url_name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
    def url_count(self):
        return ShowApiUrl.objects.count()
    
class CategoryApi(models.Model):
    name = models.CharField(max_length=40)
    api_category = models.ManyToManyField('ShowApiUrl')
    
    def __str__(self):
        return self.name
