from rest_framework import serializers
from blog.models import Post


class PostSerializer(serializers.HyperlinkedModelSerializer):
    """
        Classe que serializa os dados dos Post's
    """
    class Meta:
        model = Post
        fields = ('titulo', 'texto', 'created_on', 'updated_on')

