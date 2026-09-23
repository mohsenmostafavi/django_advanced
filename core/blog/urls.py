from django.urls import path, include
from . import views

app_name = "blog"
urlpatterns = [
    path("post/", views.PostListView.as_view(), name="list view"),
    path("post/<int:pk>", views.PostDetailView.as_view(), name="detail view"),
    path("post/create/", views.PostCreateView.as_view(), name="contact view"),
    path("post/<int:pk>/update", views.PostUpdateView.as_view(), name="edit_view"),
    path("post/<int:pk>/delete", views.PostDeleteView.as_view(), name="delete_view"),
    path("api/v1/", include("blog.api.v1.urls", namespace="api/v1")),
]
