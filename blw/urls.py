from django.urls import path
from . import views

urlpatterns = [
    # Foods
    path("", views.FoodListView.as_view(), name="food_list"),  # /blw/
    path("foods/<int:pk>/", views.FoodDetailView.as_view(), name="food_detail"),
    path("foods/add/", views.FoodCreateView.as_view(), name="food_add"),

    # Meals
    path("meals/", views.MealListView.as_view(), name="meal_list"),
    path("meals/add/", views.MealCreateView.as_view(), name="meal_add"),

    # Reactions
    path("reactions/", views.ReactionListView.as_view(), name="reaction_list"),
    path("reactions/add/", views.ReactionCreateView.as_view(), name="reaction_add"),
]


