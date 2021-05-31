from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from advertisements.models import Advertisement
from advertisements.serializers import AdvertisementSerializer
from advertisements.filters import AdvertisementFilter
from advertisements.permissions import IsOwnerOrAdmin



class AdvertisementViewSet(ModelViewSet):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = AdvertisementFilter


    def get_permissions(self):
        """Получение прав для действий."""
        if self.action == 'create':
            return [IsAuthenticated(), ]
        elif self.action in ["update", "partial_update", "destroy"]:
            return [IsAuthenticated(), IsOwnerOrAdmin(), ]
        else:
            return []

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def get_queryset(self):
        queryset = Advertisement.objects.filter(status__in=["OPEN", "CLOSED"])
        if self.request.user.is_authenticated:
            draft = Advertisement.objects.filter(status="DRAFT", creator=self.request.user).order_by('-updated_at',
                                                                                                     '-created_at')
            return queryset | draft
        return queryset