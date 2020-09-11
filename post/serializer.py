from rest_framework import serializers
from .models import Posts


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'author', 'title', 'isbn', 'released')
        model = Posts
