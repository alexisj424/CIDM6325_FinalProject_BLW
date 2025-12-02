from django.contrib import admin
from .models import Baby, Food, Meal, Reaction

@admin.register(Baby)
class BabyAdmin(admin.ModelAdmin):
    list_display = ("name", "birthday")
    search_fields = ("name",)
    list_filter = ("birthday",)

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "is_allergen")
    list_filter = ("category", "is_allergen")
    search_fields = ("name",)

class MealFoodsInline(admin.TabularInline):
    model = Meal.foods.through
    extra = 1

@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    list_display = ("baby", "date")
    list_filter = ("date", "baby")
    inlines = [MealFoodsInline]
    exclude = ("foods",)  # managed via the inline above

@admin.register(Reaction)
class ReactionAdmin(admin.ModelAdmin):
    list_display = ("baby", "food", "reaction_type", "severity", "date")
    list_filter = ("reaction_type", "severity", "date", "food", "baby")
    search_fields = ("baby__name", "food__name", "notes")

