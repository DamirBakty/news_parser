from rest_framework.response import Response
from rest_framework import generics, permissions
from rest_framework.views import APIView
from .serializers import ItemListSerializer
from .models import Item
from .parsers import parse_scientific_ru

class GetNews(APIView):
    permission_classes = [permissions.AllowAny,]

    def get(self, request):
        news = parse_scientific_ru(link="https://scientificrussia.ru")
        items = [Item(**i) for i in news]
        if news:
            Item.objects.bulk_create(objs=items)
        return Response('ok')


class ListNews(generics.ListAPIView):
    serializer_class = ItemListSerializer
    queryset = Item.objects.all()
