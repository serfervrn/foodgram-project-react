from djoser.views import UserViewSet
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Follow, User
from .serializers import (FollowListSerializer, FollowSerializer,
                          CustomUserSerializer)
from api.pagination import CustomPagination


class CastomUserViewSet(UserViewSet):
    pagination_class = CustomPagination
    serializer = CustomUserSerializer
    def get_permissions(self):
        if self.action == 'subscribe' or self.action == 'subscriptions':
            self.permission_classes = (IsAuthenticated, )
        return super().get_permissions()

    @action(detail=False)
    def subscriptions(self, request, pk=None):
        subscriptions_list = self.paginate_queryset(
            User.objects.filter(author__user=request.user)
        )
        serializer = FollowListSerializer(
            subscriptions_list, many=True, context={
                'request': request
            }
        )
        return self.get_paginated_response(serializer.data)

    @action(detail=True, methods=['POST', 'DELETE'])
    def subscribe(self, request, id):
        if request.method != 'POST':
            subscription = get_object_or_404(
                Follow,
                author=get_object_or_404(User, id=id),
                user=request.user
            )
            self.perform_destroy(subscription)
            return Response(status=status.HTTP_204_NO_CONTENT)
        serializer = FollowSerializer(
            data={
                'user': request.user.id,
                'author': get_object_or_404(User, id=id).id
            },
            context={'request': request}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
