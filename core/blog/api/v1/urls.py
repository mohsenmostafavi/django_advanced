from django.urls import path, include
from . import views

app_name = "api_v1"
urlpatterns = [
    path(
        "post/",
        views.PostViewSet.as_view({"get": "list", "post": "create"}),
        name="post_list",
    ),
    path(
        "post/<int:pk>",
        views.PostViewSet.as_view(
            {"get": "reterive", "put": "update", "delete": "destroy"}
        ),
        name="post_update",
    ),
]
