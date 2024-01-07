from main.permissions import IsActive
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from main.models import ChainLink
from main.serializers import ChainListSerializer, ChainCreateSerializer, ChainRetrieveSerializer, ChainUpdateSerializer


class ChainApiView(ListAPIView):
    queryset = ChainLink.objects.all()
    serializer_class = ChainListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["country", "company"]
    ordering_fields = ['creation']
    permission_classes = [IsActive]


class ChainCreateApi(CreateAPIView):
    serializer_class = ChainCreateSerializer
    permission_classes = [IsActive]

    def perform_create(self, serializer):
        new = serializer.save()
        if not new.provider:
            new.relationship_level = 0
            new.debt = 0.00
            new.company = "factory"
        else:
            new.relationship_level = ChainLink.objects.get(id=new.provider.id).relationship_level + 1
            new.debt = round(new.debt, 2)
        new.save()


class ChainRetrieveApiView(RetrieveAPIView):
    queryset = ChainLink.objects.all()
    serializer_class = ChainRetrieveSerializer
    permission_classes = [IsActive]


class ChainUpdateApiView(UpdateAPIView):
    queryset = ChainLink.objects.all()
    serializer_class = ChainUpdateSerializer
    permission_classes = [IsActive]


class ChainDestroyApiView(DestroyAPIView):
    queryset = ChainLink.objects.all()
    permission_classes = [IsActive]
