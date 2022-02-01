from pickletools import read_long1
from .models import Post
from rest_framework import serializers

class PostSerializer(serializers.HyperlinkedModelSerializer):    
    class Meta:
        model = Post
        fields = ['id', 'title', 'body']
