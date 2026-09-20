from django.urls import path, include
from . import views

app_name = "api_v1"
urlpatterns = [
    # path("post/", views.postList, name="post_list"),
    path("post/", views.PostList.as_view(), name="post_list"),
    path("post/<int:pk>/", views.PostDetail.as_view(), name="post_detail"),
]
