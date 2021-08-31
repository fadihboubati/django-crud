from django.urls import path, include
from fav_food.views import HomeView, DishDetailView, DishCreateView, DishUpdateView, DishDeleteView, AboutUsView

urlpatterns = [
    # path('', HomeView.as_view(), name='home'),
    # path('<int:pk>/', DetailsView.as_view(), name='detail'),
    # path('new/', addFoodLovers.as_view(), name='add'),

    path('home/',HomeView.as_view(),name='home'),
    path('dish/<int:pk>',DishDetailView.as_view(),name='dish_details'),
    path('dish/new',DishCreateView.as_view(),name='create_view'),
    path('dish/<int:pk>/update',DishUpdateView.as_view(),name='update_view'),
    path('dish/<int:pk>/delete',DishDeleteView.as_view(),name='delete_view'),
    path('aboutUs/', AboutUsView.as_view(), name='aboutUs'),
]
