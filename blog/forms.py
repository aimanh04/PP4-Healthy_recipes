from .models import Comment, Recipe
from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

    
class RecipeForm(forms.ModelForm):
    """
    Form for adding a new recipe post
    """
    class Meta:
        model = Recipe
        fields = [
            'title',
            'excerpt', 
            'featured_image',
            'prep_time',
            'cook_time',
            'servings',
            'ingredients',
            'instructions',
            'notes' 
        ]
        widgets = {
            'ingredients': SummernoteWidget(attrs={"class": "form-control"}),
            'instructions': SummernoteWidget(attrs={"class": "form-control"}),
        }
    