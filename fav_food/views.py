from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Menu

class AboutUsView(TemplateView):
    template_name = 'about_us.html'
    

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

class DishDeleteView(DeleteView):
    template_name = 'delete.html'
    model = Menu
    fields = ['user', 'name', 'fav_drink', 'fav_meal', 'eating_frequency_per_day', 'like_spicy']
    success_url = reverse_lazy('home') # after click submit and delete, redirect to the 'home' endpoint

class DishUpdateView(UpdateView):
    template_name = 'update.html'
    model = Menu
    # fields = ['user', 'name', 'fav_drink', 'fav_meal', 'eating_frequency_per_day', 'like_spicy']
    fields = '__all__'
    # here we did not determind where should redirect after submit, so will go to ...
