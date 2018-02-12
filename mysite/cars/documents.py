# documents.py

from django_elasticsearch_dsl import DocType, Index
from .models import Car

# Name of the Elasticsearch index
car = Index('cars')
# See Elasticsearch Indices API reference for available settings
car.settings(
    number_of_shards=1,
    number_of_replicas=0
)


@car.doc_type
class CarDocument(DocType):
    class Meta:
        model = Car # The model associated with this DocType

        # The fields of the model you want to be indexed in Elasticsearch
        fields = [
            'id',
            'created'
        ]

        # Ignore auto updating of Elasticsearch when a model is saved
        # or deleted:
        # ignore_signals = True
        # Don't perform an index refresh after every update (overrides global setting):
        # auto_refresh = False
        # Paginate the django queryset used to populate the index with the specified size
        # (by default there is no pagination)
        # queryset_pagination = 5000