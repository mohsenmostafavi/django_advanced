from django.contrib.auth import get_user_model
from django.db import models
from accounts.models import Profile

# getting user model object
User = get_user_model()


class Post(models.Model):
    """
    this class is table of database to define posts for blog app
    """

    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    category = models.ForeignKey("Category", on_delete=models.SET_NULL, null=True)
    status = models.BooleanField(default=False)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField()

    def __str__(self):
        return f"{self.title}: {self.content[:15]}"


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
