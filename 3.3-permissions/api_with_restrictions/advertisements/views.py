from django.http import JsonResponse
from django_filters import DateFromToRangeFilter
from django_filters.rest_framework import DjangoFilterBackend, FilterSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from advertisements.filters import AdvertisementFilter
from advertisements.models import Advertisement, Favorites
from advertisements.permissions import IsOwner
from advertisements.serializers import AdvertisementSerializer, FavoriteSerializer


class FavoritesViewSet(ModelViewSet):
    queryset = Favorites.objects.all()
    serializer_class = FavoriteSerializer

class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    #   сериализаторов и фильтров
    queryset = Advertisement.objects.exclude(status='DRAFT')
    serializer_class = AdvertisementSerializer
    filter_backends = [DjangoFilterBackend, ]
    filterset_class = AdvertisementFilter

    def get_queryset(self):
        if self.request.user.is_authenticated:
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

    @action(methods=['POST'], detail=True)
    def favorite(self, request, pk=None):
        if self.request.user.id == Advertisement.objects.get(id=pk).creator_id:
            raise ValidationError('Свои объявления нельзя сохранить в избранном')

        fav = Favorites(
            user_id=self.request.user.id,
            advertisement_id=pk,
        )
        fav.save()
        return Response(FavoriteSerializer(fav).data)


