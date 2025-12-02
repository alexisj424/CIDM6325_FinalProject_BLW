from django import forms
from .models import Food, Meal, Reaction

class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ["name", "category", "is_allergen", "image"]

class MealForm(forms.ModelForm):
    class Meta:
        model = Meal
        fields = ["baby", "date", "foods", "notes", "photo"]
        widgets = {
            "date": forms.DateInput(attrs={"type": "date"}),
        }

class ReactionForm(forms.ModelForm):
    class Meta:
        model = Reaction
        fields = ["baby", "food", "reaction_type", "severity", "date", "notes"]
        widgets = {
            "date": forms.DateInput(attrs={"type": "date"}),
        }
