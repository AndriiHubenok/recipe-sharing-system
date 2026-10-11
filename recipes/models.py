from django.db import models

class Recipe(models.Model):

    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='recipe_images/')
    description = models.TextField()
    calories = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title

class Product(models.Model):

    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

class Ingredient(models.Model):

    class Unit(models.TextChoices):
        PIECES = 'pcs', 'Pieces'
        MILLIGRAMS = 'mg', 'Milligrams'
        GRAMS = 'g', 'Grams'
        KILOGRAMS = 'kg', 'Kilograms'
        OUNCES = 'oz', 'Ounces'
        POUNDS = 'lb', 'Pounds'
        MILLILITERS = 'ml', 'Milliliters'
        LITERS = 'l', 'Liters'
        TEASPOONS = 'tsp', 'Teaspoons'
        TABLESPOONS = 'tbsp', 'Tablespoons'
        CUPS = 'cup', 'Cups'
        PINTS = 'pt', 'Pints'
        QUARTS = 'qt', 'Quarts'
        GALLONS = 'gal', 'Gallons'

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='ingredients')
    amount = models.IntegerField()
    unit = models.CharField(max_length=50, choices=Unit.choices, default=Unit.PIECES)

    def __str__(self) -> str:
        return f"{self.product.name} - {self.amount} {self.unit}"