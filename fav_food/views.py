from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Menu

# Create your views here.
class HomeView(ListView):
    template_name = 'home.html'
    model = Menu

class DishDetailView(DetailView):
    template_name = 'details.html'
    model = Menu

class DishCreateView(CreateView):
    template_name = 'add.html'
    model = Menu
    fields = ['user', 'name', 'fav_drink', 'fav_meal', 'eating_frequency_per_day', 'like_spicy']

class DishUpdateView(CreateView):
    template_name = 'update.html'
    model = Menu
    fields = ['user', 'name', 'fav_drink', 'fav_meal', 'eating_frequency_per_day', 'like_spicy']

class DishDeleteView(DeleteView):
    template_name = 'delete.html'
    model = Menu
    fields = ['user', 'name', 'fav_drink', 'fav_meal', 'eating_frequency_per_day', 'like_spicy']
    success_url = reverse_lazy('home')