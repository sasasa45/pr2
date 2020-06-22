from rest_framework import viewsets, filters
from .serializers import ItemsSerializer
from item.models import Items
from rest_framework.response import Response
# class ItemsViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset=Items.objects.all()
#     serializer_class=ItemsSerializer
#     filter_backends=[filters.SearchFilter]
#     search_fields=['name','text']
class ItemsViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Items.objects.all()
        serializer = ItemsSerializer(queryset, many=True,context={'request': request})
        return Response(serializer.data)
