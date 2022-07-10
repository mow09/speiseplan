from django.contrib import admin
from food.models import (
    Allergy,
    Additive,
    Category,
    Region,
    Ingredient,
    Meal,
)


class AllergyAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)
    search_fields = ['name']


class AdditiveAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)
    search_fields = ['name']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)
    search_fields = ['name']


class RegionAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)
    search_fields = ['name']


class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)
    search_fields = ['name']


class MealAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('name', 'show', 'price', 'bio', 'vegan', 'vegetarian', 'region',)
    autocomplete_fields = ['category', 'ingredients', 'additives', 'allergies', 'region', ]

    fieldsets = (
        (None, {'fields': ('name', 'show')}),
        ('Details ', {'fields': ('description', 'category', 'price',)}),
        ('Genaueres', {'fields': ('special_offer', 'bio', 'vegan', 'vegetarian',)}),
        (None, {'fields': ('region', 'saisonal_month', 'ingredients', 'additives', 'allergies',)}),
    )


admin.site.register(Allergy, AllergyAdmin)
admin.site.register(Additive, AdditiveAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Region, RegionAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Meal, MealAdmin)
