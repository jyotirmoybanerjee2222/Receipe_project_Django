from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [

    path('token/', obtain_auth_token, name='api-token'),
    path('recipes/', views.recipe_list_create, name='recipe-list-create'),
    path('recipes/<int:pk>/', views.recipe_detail, name='recipe-detail'),
    path('recipes/sample/', views.sample_recipe, name='sample-recipe'),
]
