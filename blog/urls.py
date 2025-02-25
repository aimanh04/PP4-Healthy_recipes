from django.urls import path
from . import views

urlpatterns = [
    path('', views.RecipeList.as_view(), name='home'),
    path('add_recipe/', views.RecipeAdd.as_view(), name='add_recipe'),
    path('<slug:slug>/', views.recipe_detail, name='recipe_detail'),
    path('edit-recipe/<slug:slug>', views.EditRecipe.as_view(), name='edit_recipe'),
    path('delete-recipe/<slug:slug>', views.DeleteRecipe.as_view(), name='delete_recipe'),
    path('<slug:slug>/edit_comment/<int:comment_id>',
         views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>',
         views.comment_delete, name='comment_delete'),
     path('like/<slug:slug>', views.RecipeLikes.as_view(), name='recipe_likes'),
]