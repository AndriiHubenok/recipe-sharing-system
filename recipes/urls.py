from django.urls import path, include
from rest_framework import routers

from recipes.views import RecipeViewSet, IngredientViewSet, ProductViewSet

router = routers.DefaultRouter()
router.register(r'recipes', RecipeViewSet)
router.register(r'ingredients', IngredientViewSet)
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
]