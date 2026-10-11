from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from recipes.models import Recipe, Ingredient, Product
from recipes.serializers import RecipeSerializer, IngredientSerializer, ProductSerializer

class RecipePagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    def get_queryset(self):
        queryset = super().get_queryset()

        name = self.request.query_params.get('name')
        if name:
            queryset = queryset.filter(title__icontains=name)

        product_id = self.request.query_params.get('product_id')
        if product_id:
            ids = [int(id) for id in product_id.split(',') if id.isdigit()]
            for id in ids:
                queryset = queryset.filter(ingredients__product__id=id)

        product_name = self.request.query_params.get('product_name')
        if product_name:
            queryset = queryset.filter(ingredients__product__name__icontains=product_name)

        description = self.request.query_params.get('description')
        if description:
            queryset = queryset.filter(description__icontains=description)

        return queryset


class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

    def get_queryset(self):
        queryset = super().get_queryset()

        recipe_id = self.request.query_params.get('recipe_id')
        if recipe_id:
            queryset = queryset.filter(recipe_id=recipe_id)

        return queryset


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = super().get_queryset()

        name = self.request.query_params.get('name')
        if name:
            queryset = queryset.filter(name__icontains=name)

        return queryset
