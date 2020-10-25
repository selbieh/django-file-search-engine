from django.template import loader
from haystack import indexes

from .models import StoredFiles

from tika import parser


class StoredFilesIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    title_index = indexes.CharField(model_attr='title')
    file_index = indexes.CharField(model_attr='file')

    def get_model(self):
        return StoredFiles

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()

    @staticmethod
    def parsed_file(file):
        parsed = parser.from_file(file.path)
        return {
            "metadata": parsed["metadata"],
            "content": parsed['content']
        }

    def prepare(self, obj):
        data = super(StoredFilesIndex, self).prepare(obj)
        file_obj = obj.file
        extracted_data = self.parsed_file(file_obj)
        t = loader.select_template(('search/indexes/heystack_search/storedfiles_text.txt',))
        data['text'] = t.render({'object': obj,
                                 'extracted': extracted_data})

        return data
