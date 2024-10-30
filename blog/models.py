from django.db import models


class UserModel(models.Model):
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    username = models.CharField(max_length=55)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.username} : {self.first_name} {self.last_name}"

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class BlogModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    author = models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True, blank=True)
    written_date = models.PositiveIntegerField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.author}"

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'


class CommentsModel(models.Model):
    description = models.TextField()
    author = models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True, blank=True)
    blog = models.ForeignKey(BlogModel, on_delete=models.CASCADE, null=True, blank=True)
    written_date = models.PositiveIntegerField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.blog} - {self.author}"

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

