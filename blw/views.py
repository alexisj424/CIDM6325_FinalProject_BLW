from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy

from .models import Food, Meal, Reaction
from .forms import FoodForm, MealForm, ReactionForm

# BEST: cache food list for 15 minutes
@method_decorator(cache_page(60 * 15), name="dispatch")
class FoodListView(ListView):
    model = Food
    template_name = "blw/foods/list.html"
    context_object_name = "foods"
    paginate_by = 10


class FoodDetailView(DetailView):
    model = Food
    template_name = "blw/foods/detail.html"
    context_object_name = "food"


class FoodCreateView(LoginRequiredMixin, CreateView):
    model = Food
    form_class = FoodForm
    template_name = "blw/foods/form.html"
    success_url = reverse_lazy("food_list")


class MealListView(ListView):
    model = Meal
    template_name = "blw/meals/list.html"
    context_object_name = "meals"
    paginate_by = 10


class MealCreateView(LoginRequiredMixin, CreateView):
    model = Meal
    form_class = MealForm
    template_name = "blw/meals/form.html"
    success_url = reverse_lazy("meal_list")


class ReactionListView(ListView):
    model = Reaction
    template_name = "blw/reactions/list.html"
    context_object_name = "reactions"
    paginate_by = 10


class ReactionCreateView(LoginRequiredMixin, CreateView):
    model = Reaction
    form_class = ReactionForm
    template_name = "blw/reactions/form.html"
    success_url = reverse_lazy("reaction_list")


# Create your views here.
