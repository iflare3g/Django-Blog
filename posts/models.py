from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=120)
    body = models.TextField()
    date = models.DateTimeField(auto_now=False,auto_now_add=True)
    slug = models.SlugField()
    
    def __str__(self):
        return self.title
        
    # Best practice per ottenere la url del singolo post
    def get_absolute_url(self):
        return reverse("single",kwargs={ 'id': self.id , 'slug': self.slug })