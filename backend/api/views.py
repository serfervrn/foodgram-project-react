from django.shortcuts import render
from djoser.views import UserViewSet

from users.models import User


# Create your views here.

class UserView(UserViewSet):

    # serializer_class = RegistrationSerializer

    def get_queryset(self):
        return User.objects.all()

class TagViewSet():
    pass


class IngredientViewSet():
    pass

class RecipeViewSet():
    pass