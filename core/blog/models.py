from django.db import models

class Post(models.Model):
    author = models.ForeignKey('User', on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    status = models.BooleanField(default=False)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField()

    def __str__(self):
        return f'{self.title}: {self.content[:15]}'

class Categgory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
