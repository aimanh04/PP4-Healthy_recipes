from django.urls import path
from . import views

urlpatterns = [
    path('', views.RecipeList.as_view(), name='home'),
    path('<slug:slug>/', views.recipe_detail, name='recipe_detail'), 
]