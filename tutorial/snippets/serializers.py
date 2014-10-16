from django.forms import widgets
from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style')

    # def restore_object(self, attrs, instance=None):
    #     """
    #     create or update a new snippet instance, given dictionary of deserialized field values
    #     without this method desrializing will simply return a dict of items
    #     """
    #
    #     if instance:
    #         #update it
    #         instance.title = attrs.get('title', instance.title)
    #         instance.code = attrs.get('code', instance.code)
    #         instance.linenos = attrs.get('linenos', instance.linenos)
    #         instance.language  = attrs.get('language', instance.language)
    #         instance.style = attrs.get('style', instance.style)
    #
    #         return instance
    #
    #     #create new instance
    #     return Snippet(**attrs)

        #request.POST  # Only handles form data.  Only works for 'POST' method.
        #request.DATA  # Handles arbitrary data.  Works for 'POST', 'PUT' and 'PATCH' methods.