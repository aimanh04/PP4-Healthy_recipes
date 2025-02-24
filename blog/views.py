from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.views.generic import ListView, CreateView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.text import slugify
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from .models import Recipe, Comment, RecipeLikes, User
from .forms import CommentForm, RecipeForm


class RecipeList(generic.ListView):
    """ 
    Retrieves all published recipes from :model:blog.Recipe 
    and displays them with a pagination limit of 9 posts per page.
    """
    queryset = Recipe.objects.filter(status=1)
    # queryset = Recipe.objects.all()
    template_name = "blog/index.html"
    paginate_by = 9
    
    
def recipe_detail(request, slug):
    """
    Displays a single recipe post from :model:`blog.Recipe`.

    **Context Variables:**
    - ``recipe``: The recipe instance.  
    - ``comments``: Approved comments for the recipe.  
    - ``total_comments``: Total count of approved comments.  
    - ``comment_form``: A :form:`blog.CommentForm` instance.  

    **Template:**  
    :template:`blog/recipe_detail.html`
    """

    queryset = Recipe.objects.filter(status=1)
    recipe = get_object_or_404(queryset, slug=slug)
    comments = recipe.comments.all().order_by("-created_on")
    # comment_count = recipe.comments.filter(approved=True).count()
    comment_count = recipe.comments.count()
    comment_form = CommentForm()
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.recipe = recipe
            comment.save()
            #messages.add_message(
            #    request, messages.SUCCESS,
            #    'Comment submitted and awaiting approval'
            # )
            messages.success(request, 'Comment was posted successfully!')
            comment_count = recipe.comments.count()

    comment_form = CommentForm()

    return render(
        request,
        "blog/recipe_detail.html",
        {
            "recipe": recipe,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        }
    )

class RecipeLikes(View):
    """
    View to handle the like functionality for Posts
    """
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Recipe, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('recipe_detail', args=[slug]))


def comment_edit(request, slug, comment_id):
    """
    view to edit comments
    """
    if request.method == "POST":

        queryset = Recipe.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('recipe_detail', args=[slug]))


def comment_delete(request, slug, comment_id):
    """
    View to delete comments on the Recipe Posts
    """
    queryset = Recipe.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Your comment has been deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('recipe_detail', args=[slug]))


class RecipeAdd(SuccessMessageMixin, CreateView):
    """
    View to add a new recipe post
    """
    model = Recipe
    template_name = 'add_recipe.html'
    form_class = RecipeForm
    success_url = reverse_lazy("home")
    success_message = 'Recipe added successfully!'

    def form_valid(self, form):
        """
        Assign the current user to the author field"""
        form.instance.author = self.request.user
        return super().form_valid(form)