from django.db import models
from django.contrib.auth.models import User

SERVINGS = [tuple([x,x]) for x in range(1,7)]
STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.
class Recipe(models.Model):
    
    """
    Stores a single Recipe post entered by user related to :model:`auth.User`.
    """

    title = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="recipe_posts"
    )
    # featured_image = CloudinaryField('image', default='placeholder')
    prep_time = models.CharField(max_length=100)
    cook_time = models.CharField(max_length=100)
    servings = models.IntegerField(choices=SERVINGS)
    ingredients = models.TextField(blank=True)
    instructions = models.TextField()
    excerpt = models.TextField(blank=True)
    notes = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on", "author"]
    def __str__(self):
        return f"Recipe name: {self.title} | Recipe added by: {self.author}"


class Comment(models.Model):
    """
    Stores a comment entered by a user related to :model:`auth.User`
    and :model:`blog.Recipe`.
    """
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name="comments"
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter"
    )
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]
    def __str__(self):
        return f"Comment: {self.body} | Comment left by: {self.author}"