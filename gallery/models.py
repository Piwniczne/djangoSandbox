from email.policy import default
from operator import mod
from statistics import mode
from django.db import models
from django.template.defaultfilters import slugify
from django_resized import ResizedImageField
from django.utils import timezone
from uuid import uuid4
# from django.conf import settings
from django.urls import reverse
# import json
# import os


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



class Image(models.Model):
    description = models.TextField(null=True, blank=True)
    altText = models.TextField(null=True, blank=True)
    hashTags = models.CharField(null=True, blank=True, max_length=300)

    #ImageFields
    squareImage = ResizedImageField(size=[1000, 1000], crop=['middle', 'center'], default='default_square.jpg', upload_to='square')
    landImage = ResizedImageField(size=[2878, 1618], crop=['middle', 'center'], default='default_land.jpg', upload_to='landscape')
    tallImage  = ResizedImageField(size=[1618, 2878], crop=['middle', 'center'], default='default_tall.jpg', upload_to='tall')

    #Related Fields
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE)

    #Utility variable
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    dataCreated = models.DateTimeField(blank=True, null=True)
    lastUpdated = models.DateTimeField(blank=True, null=True)


    def __str__(self):
        return '{} {}'.format(self.category.title, self.uniqueId)


    def get_absolute_url(self):
        return reverse('gallery-image-detail', kwargs={'slug': self.slug})


    def save(self, *args, **kwargs):
        if self.dataCreated is None:
            self.dataCreated = timezone.localtime(timezone.now())
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
            self.slug = slugify('{} {}'.format(self.category.title, self.uniqueId))


        self.slug = slugify('{} {}'.format(self.category.title, self.uniqueId))
        self.lastUpdated = timezone.localtime(timezone.now())
        super(Image, self).save(*args, **kwargs)