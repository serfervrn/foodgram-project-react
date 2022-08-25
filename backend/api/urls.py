from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken import views
from api.views import UserView, TagViewSet, IngredientViewSet, RecipeViewSet

app_name = 'api'

router = routers.DefaultRouter()
router.register('users',  UserView, basename='users')
# router.register('tags', TagViewSet, basename='tags')
# router.register('ingredients', IngredientViewSet, basename='ingredients')
# router.register('recipes', RecipeViewSet, basename='recipes')


urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls.authtoken')),
]
