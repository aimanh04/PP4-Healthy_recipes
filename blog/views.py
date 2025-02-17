from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Recipe


class RecipeList(generic.ListView):
    """
    Returns all published recipes in :model:`blog.Recipe`
    and displays them in a page of 9 posts per page. 
    """
    queryset = Recipe.objects.filter(status=1)
    # queryset = Recipe.objects.all()
    template_name = "blog/index.html"
    paginate_by = 9
    
    
def recipe_detail(request, slug):
    """
    Handles the display of a single recipe post from :model:`blog.Recipe`.

    **Context Variables:**
    - ``recipe``: An instance of :model:`blog.Recipe`.
    - ``comments``: Approved comments associated with the recipe.
    - ``total_comments``: Count of approved comments for the recipe.
    - ``comment_form``: An instance of :form:`blog.CommentForm`.

    **Template Used:**  
    :template:`blog/recipe_detail.html`
    """

    queryset = Recipe.objects.filter(status=1)
    recipe = get_object_or_404(queryset, slug=slug)
    comments = recipe.comments.all().order_by("-created_on")
    total_comments = recipe.comments.filter(approved=True).count()

    return render(
        request,
        "blog/recipe_detail.html",
        {
            "recipe": recipe,
            "comments": comments,
            "total_comments": total_comments,
        }
        # {"recipe": recipe,
        #  "coder": "Matt Rudge"},
    )