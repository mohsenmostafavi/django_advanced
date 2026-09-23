from django.contrib import admin
from blog.models import Post, Category


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    empty_value_display = "-empty-"
    list_display = ["author", "title", "status"]


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
