from django.forms import widgets
from core import serializers as custom_serializers
from datapoint.models import Datapoint, Annotation
from rest_framework import serializers


class TaggedModelSerializer(serializers.ModelSerializer):
    """
    xaralis's solution from https://github.com/alex/django-taggit/issues/223

    Rest framework doesn't work with django taggit very well since it is not
    ready for fields being in fact TaggitManager instance.

    This class solves it by pulling out the incorrectly resolved data and saving
    them manually thereafter.
    """
    tag_fields = ['tags']

    def save_object(self, obj, **kwargs):
        tags_to_set = {}

        # Try to find tag data.
        if getattr(obj, '_m2m_data', None):
            for f in self.tag_fields:
                if f in obj._m2m_data:
                    # pop() is important. We don't want the data to be set by
                    # rest framework.
                    tags_to_set[f] = obj._m2m_data.pop(f)

        # When data has been cleaned, save the object as usual.
        super(TaggedModelSerializer, self).save_object(obj, **kwargs)

        # If some tag data was previously found, save them now.
        for f, tags in tags_to_set.items():
            # Pull out the tag manager class.
            mngr = getattr(obj, f)

            # Decide which class for tags is being used.
            TagClass = mngr.through.tag.field.rel.to
            tgs = TagClass.objects.filter(slug__in=tags)

            # Finally, set the data using manager class.
            mngr.set(*tgs)


class DatapointSerializer(TaggedModelSerializer):
    class Meta:
        model = Datapoint
        fields = ('pk', 'owner', 'project', 'collections', 'name', 'description', 'author', 'source', 'url',
                                                        'publish_date')


class AnnotationSerializer(TaggedModelSerializer):
    class Meta:
        model = Annotation
        fields = ('pk', 'owner', 'datapoint', 'annotator_schema_version', 'text', 'quote', 'uri', 'range_start',
				        				'range_end', 'range_startOffset', 'range_endOffset')
