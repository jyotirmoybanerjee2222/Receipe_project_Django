from django.urls import path
from . import views

urlpatterns = [
    path('recipes/', views.recipe_list_create, name='recipe-list-create'),
    path('recipes/<int:pk>/', views.recipe_detail, name='recipe-detail'),
    path('recipes/sample/', views.sample_recipe, name='sample-recipe'),
]
