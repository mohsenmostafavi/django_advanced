from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

app_name = "api_v1"

router = DefaultRouter()
router.register("post", views.PostViewSet, basename="post")
urlpatterns = router.urls

"""
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
"""
