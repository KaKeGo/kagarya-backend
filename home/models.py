from django.db import models

# Create your models here.


class ShowApiUrl(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=255, null=True, blank=True)
    url_name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
    def Url_count(self):
        return ShowApiUrl.objects.count()
    
class CategoryApi(models.Model):
    name = models.CharField(max_length=40)
    api_category = models.ManyToManyField('ShowApiUrl')
    
    def __str__(self):
        return self.name
