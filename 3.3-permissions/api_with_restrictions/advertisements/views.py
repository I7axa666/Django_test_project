from django.http import JsonResponse
from django_filters import DateFromToRangeFilter
from django_filters.rest_framework import DjangoFilterBackend, FilterSet
from requests import Response
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from advertisements.models import Advertisement
from advertisements.permissions import IsOwner
from advertisements.serializers import AdvertisementSerializer


class AdvertisementFilter(FilterSet):
    created_at = DateFromToRangeFilter()

    class Meta:
        model = Advertisement
        fields = ['creator', 'status', 'created_at', 'favorite']

class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    #   сериализаторов и фильтров
    queryset = Advertisement.objects.exclude(status='DRAFT')
    serializer_class = AdvertisementSerializer
    filter_backends = [DjangoFilterBackend, ]
    # filterset_fields = ['creator']
    filterset_class = AdvertisementFilter

    def get_queryset(self):
        if IsAuthenticated():
            creator_id = self.request.user.id
            queryset = Advertisement.objects.filter(creator_id=creator_id)
            return queryset
        else:
            queryset = Advertisement.objects.exclude(status='DRAFT')
            return queryset

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [IsAuthenticated(), IsOwner()]
        return []

    @action(methods=['PATCH'], detail=True)
    def favorite(self, request, pk=None):
        if self.request.user.id == Advertisement.objects.get(id=pk).creator_id:
            raise ValidationError('Свои объявления нельзя сохранить в избранном')

        instance = Advertisement.objects.get(id=pk)
        instance.favorite = request.data['favorite']
        instance.save()
        serializers = self.get_serializer(Advertisement.objects.get(id=pk))
        return Response(serializers.data)