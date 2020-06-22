from rest_framework import serializers
from item.models import Items

class ItemsSerializer(serializers.ModelSerializer):
    image=serializers.SerializerMethodField()
    category=serializers.SerializerMethodField()
    # url=serializers.HyperlinkedModelSerializer(view_name='items-detail', lookup_field='pk')
    class Meta:
        model=Items
        fields=['id','url','name','price','text','image','category']
        extra_kwargs = {
            'url': {'view_name': 'item-api:list', 'lookup_field': 'pk'},
        }
    def get_image(self, obj):
        return obj.picture_changed.url
    def get_category(self,obj):
        return obj.category.name
