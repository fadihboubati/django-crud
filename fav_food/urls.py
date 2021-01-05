from django.urls import path, include
from fav_food.views import HomeView, DishDetailView, DishCreateView, DishUpdateView, DishDeleteView

urlpatterns = [
    # path('', HomeView.as_view(), name='home'),
    # path('<int:pk>/', DetailsView.as_view(), name='detail'),
    # path('new/', addFoodLovers.as_view(), name='add'),

    path('',HomeView.as_view(),name='home'),
    path('home/<int:pk>',DishDetailView.as_view(),name='dish_details'),
    path('dish/new',DishCreateView.as_view(),name='create_view'),
    path('dish/<int:pk>/update',DishUpdateView.as_view(),name='update_view'),
    path('dish/<int:pk>/delete',DishDeleteView.as_view(),name='delete_view'),
]
