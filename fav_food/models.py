from django.db import models
from django.urls import reverse

# Create your models here.
class Menu (models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    fav_drink = models.CharField(max_length=64)
    fav_meal = models.CharField(max_length=64)
    eating_frequency_per_day = models.IntegerField()
    like_spicy = models.BooleanField()
    def __str__(self):
        return self.name
    def get_absolute_url (self):
        return reverse('home')
        #return reverse('detail', args=[str(self.id)])
