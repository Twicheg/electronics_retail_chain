from rest_framework.generics import ListAPIView, CreateAPIView

from main.models import ChainLink
from main.serializers import ChainListSerializer, ChainCreateSerializer


class ChainApiView(ListAPIView):
    queryset = ChainLink.objects.all()
    serializer_class = ChainListSerializer


class ChainCreateApi(CreateAPIView):
    serializer_class = ChainCreateSerializer

    def perform_create(self, serializer):
        new = serializer.save()
        new.relationship_level = ChainLink.objects.get(id=new.provider.id).relationship_level + 1
        new.debt = round(new.debt, 2)
        new.save()
