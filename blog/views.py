from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
# local
from .models import Category, Publication
from .serializers import CategorySerializer, PublicationSerializer
from .permissions import IsOwnerOrReadOnly
from .filters import CategoryFilter, PublicationFilter


class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = CategoryFilter


class CategoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class PublicationListCreateAPIView(generics.ListCreateAPIView):
    queryset = Publication.objects.filter(is_archived=False)
    serializer_class = PublicationSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = PublicationFilter
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class PublicationRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PublicationSerializer
    queryset = Publication.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]