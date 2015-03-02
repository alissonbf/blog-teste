import datetime
from haystack import indexes
from blog.models import Post


class PostIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    titulo = indexes.CharField(model_attr='titulo')
    texto = indexes.CharField(model_attr='texto')
    created_on = indexes.DateTimeField(model_attr='created_on')

    def get_model(self):
        return Post

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(created_on__lte=datetime.datetime.now())