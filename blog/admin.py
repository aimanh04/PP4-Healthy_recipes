from django.contrib import admin
from .models import Recipe, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Recipe)
class PostAdmin(SummernoteModelAdmin):

    """
    Lists fields for display in admin, search & filter fields.
    """

    list_display = ('title', 'author', 'status', 'created_on')
    search_fields = ['title', 'ingredients',]
    list_filter = ('status', 'created_on',)
    # prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('ingredients', 'instructions',)

# Register your models here.
admin.site.register(Comment)