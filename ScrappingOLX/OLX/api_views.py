from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination

from OLX.serializer import ItemsSerializer
from OLX.models import Items
from OLX.scrapping import scrapper
class ItemsPagination(LimitOffsetPagination):
    default_limit = 30
    max_limit = 300

class ItemList(ListAPIView):
    queryset = Items.objects.all()
    serializer_class = ItemsSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('category',)
    search_fields = ('name')
    pagination_class = ItemsPagination

class ItemCreate(CreateAPIView):
    serializer_class = ItemsSerializer

    def create(self, request, *args, **kwargs):
        # try:
        #     passvalidate =  request.data.get('category')
        #     if price is not None and float(price) <= 0.0:
        #         raise ValidationError({ 'price': 'Must be above $0.00' })
        # except ValueError:
        #     raise ValidationError({ 'price': 'A valid number is required' })
        
        print("request = ",request.data.get('category'))
        return super().create(request, *args, **kwargs)

class ItemRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Items.objects.all()
    lookup_field = 'id'
    serializer_class = ItemsSerializer

    def delete(self, request, *args, **kwargs):
        item_id = request.data.get('id')
        response = super().delete(request, *args, **kwargs)
        if response.status_code == 204:
            from django.core.cache import cache
            cache.delete('item_data_{}'.format(item_id))
        return response

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        if response.status_code == 200:
            from django.core.cache import cache
            item = response.data
            cache.set('item_data_{}'.format(item['id']), {
                'name': item['name'],
                'price': item['price'],
            })
        return response