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
    pass


class AdditiveAdmin(admin.ModelAdmin):
    pass


class CategoryAdmin(admin.ModelAdmin):
    pass


class RegionAdmin(admin.ModelAdmin):
    pass


class IngredientAdmin(admin.ModelAdmin):
    pass


class MealAdmin(admin.ModelAdmin):
    pass


admin.site.register(Allergy, AllergyAdmin)
admin.site.register(Additive, AdditiveAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Region, RegionAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Meal, MealAdmin)
