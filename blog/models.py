from django.utils import timezone
from uuid import uuid4
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.template.defaultfilters import slugify
from django_resized import ResizedImageField
# Create your models here.

class Category(models.Model):
    title = models.CharField(null=True, blank=True, max_length=200)
    description = models.TextField(null=True, blank=True)

    #Utility Variable
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    dataCreated = models.DateTimeField(blank=True, null=True)
    lastUpdated = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return '{} {}'.format(self.title, self.uniqueId)

    def get_absolute_url(self):
        return reverse("category-detail", kwargs={"slug": self.slug})
        
    def save(self, *args, **kwargs):
        if self.dataCreated is None:
            self.dataCreated = timezone.localtime(timezone.now())
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
            self.slug = slugify('{} {}'.format(self.title, self.uniqueId))

        self.slug = slugify('{} {}'.format(self.title, self.uniqueId))
        self.lastUpdated = timezone.localtime(timezone.now())
        super(Category, self).save(*args, **kwargs)
        
class Post(models.Model):
    title = models.CharField(null=False, blank=True, max_length= 255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    thumbnail = ResizedImageField(size=[200, 250], crop=['middle', 'center'], default='blog/default_blog_thumbnail.jpg', upload_to='blog/')
    # used in Admin page
    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse("blog-article", kwargs={"pk": self.pk})
    