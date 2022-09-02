from django.shortcuts import get_object_or_404
from django.db.models import Sum
from django.http import HttpResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from api import filters
from api.filters import RecipeFilter, IngredientFilter
from api.pagination import CustomPagination
from api.permissions import IsAuthorOrAdminOrReadOnly
from api.serializers import TagSerializer, IngredientSerializer, \
    ShoppingCartSerializer, FavoriteSerializer, GetRecipeSerializer, \
    RecipeSerializer
from recipes.models import Tag, Ingredient, Recipe, Favorite, ShoppingCart, \
    RecipeIngredient


class TagViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tag.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = TagSerializer
    pagination_class = None



class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    permission_classes = (IsAuthorOrAdminOrReadOnly,)
    pagination_class = CustomPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_class = RecipeFilter

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return GetRecipeSerializer
        return RecipeSerializer

    @staticmethod
    def post_method_for_action(request, pk, serializers):
        data = {'user': request.user.id, 'recipe': pk}
        serializer = serializers(data=data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(methods=['POST'], detail=True,
            permission_classes=[IsAuthenticated])
    def favorite(self, request, pk):
        return self.post_method_for_action(request=request, pk=pk,
                                           serializers=FavoriteSerializer)

    @action(methods=['POST'], detail=True,
            permission_classes=[IsAuthenticated],
            )
    def shopping_cart(self, request, pk):
        return self.post_method_for_action(request=request, pk=pk,
                                           serializers=ShoppingCartSerializer)

    @staticmethod
    def delete_method_for_actions(request, pk, model):
        user = request.user
        recipe = get_object_or_404(Recipe, id=pk)
        model_object = get_object_or_404(model, user=user, recipe=recipe)
        model_object.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @favorite.mapping.delete
    def delete_favorite(self, request, pk):
        return self.delete_method_for_actions(
            request=request, pk=pk, model=Favorite
        )

    @shopping_cart.mapping.delete
    def delete_shopping_cart(self, request, pk):
        return self.delete_method_for_actions(
            request=request, pk=pk, model=ShoppingCart
        )

    @action(detail=False, permission_classes=[IsAuthenticated])
    def download_shopping_cart(self, request):
        ingredients = RecipeIngredient.objects.filter(
            recipe__shopping_cart__user=request.user).values(
            'ingredient__name',
            'ingredient__measurement_unit').annotate(total=Sum('amount'))
        content = 'Cписок покупок:\n\n'
        for number, ingredient in enumerate(ingredients, start=1):
            content += (
                f'[{number}] '
                f'{ingredient["ingredient__name"]} - '
                f'{ingredient["total"]} '
                f'{ingredient["ingredient__measurement_unit"]}\n')

        filename = 'shopping_cart.pdf'
        response = HttpResponse(content, content_type='application/pdf')
        response['Content-Disposition'] = (f'attachment;'
                                           f'filename={filename}')
        return response


class IngredientViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Ingredient.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = IngredientSerializer
    filter_backends = (IngredientFilter,)
    search_fields = ("^name",)
