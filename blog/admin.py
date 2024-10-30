from django.contrib import admin
from .models import UserModel, BlogModel, CommentsModel


@admin.register(UserModel)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'username', 'created_at', 'updated_at')
    search_fields = ('first_name', 'last_name')
    list_filter = ('username',)


@admin.register(BlogModel)
class BlogModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'description', 'created_at', 'updated_at')
    search_fields = ('title',)
    list_filter = ('title',)


@admin.register(CommentsModel)
class CommentsModelAdmin(admin.ModelAdmin):
    list_display = ('description', 'author', 'blog', 'created_at', 'updated_at')
    search_fields = ('description',)
    list_filter = ('created_at',)
