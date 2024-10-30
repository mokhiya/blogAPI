from django.urls import path

from blog.views import users, blogs, comments

app_name = 'books'

urlpatterns = [
    # users
    path('users', users.user_list_create, name='user-list-create'),
    path('users/<int:pk>', users.user_detail, name='user-detail'),

    # blogs
    path('blogs', blogs.blog_list_create, name='blog-list-create'),
    path('blogs/<int:pk>', blogs.blog_detail, name='blog-detail'),
    path('blogs/users/<int:pk>', blogs.blog_user_detail, name='blog-user-detail'),

    # comments
    path('commenst', comments.comment_list_create, name='comment-list-create'),
    path('comments/<int:pk>', comments.comment_detail, name='comment-detail'),
]
