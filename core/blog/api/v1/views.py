from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import (
    GenericAPIView,
    CreateAPIView,
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework import mixins, viewsets
from .serializers import (
    PostSerializer,
    CategorySerializer,
    #    PostDetailSerializer,
    #   PostListSerializer,
)
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .permissions import IsAuthorOrReadOnly
from .paginations import DefualtPagination
from blog.models import Post, Category


# Example Of DRF Function Base Views
"""
@api_view(["GET", "POST"])
@permission_classes(
    [
        IsAuthenticatedOrReadOnly,
    ]
)
def postList(request):
    if request.method == "GET":
        # posts = Post.objects.filter(status=True)
        posts = get_list_or_404(Post, status=True)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


@api_view(["GET", "PUT", "DELETE"])
@permission_classes(
    [
        IsAuthenticatedOrReadOnly,
    ]
)
def postDetail(request, post_id):
    post = get_object_or_404(Post, pk=post_id, status=True)
    if request.method == "GET":
        serializer = PostSerializer(post)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = PostSerializer(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == "DELETE":
        post.delete()
        return Response(
            {"detail": "item remove successfully"}, status=status.HTTP_204_NO_CONTENT
        )
"""


# Example Of DRF APIView Views
"""class PostList(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer

    def get(self, request):
        posts = get_list_or_404(Post, status=True)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class PostDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer

    def get(self, request, post_id):
        post = get_object_or_404(Post, pk=post_id, status=True)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def put(self, request, post_id):
        post = get_object_or_404(Post, pk=post_id, status=True)
        serializer = PostSerializer(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, post_id):
        post = get_object_or_404(Post, pk=post_id, status=True)
        post.delete()
        return Response(
            {"detail": "item remove successfully"}, status=status.HTTP_204_NO_CONTENT
        )        
        
        
"""

# Example Of DRF GenericView Base Views
"""
class PostList(ListAPIView, CreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)


class PostDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)

"""

# Example Of DRF ViewSet
"""
class PostViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)

    def list(self, request):
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data)

    def reterive(self, request, pk=None):
        post_object = get_object_or_404(Post, pk=pk)
        serializer = self.serializer_class(post_object)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def update(self, request, pk=None):
        post_object = get_object_or_404(Post, pk=pk)
        serializer = self.serializer_class(post_object, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        post = get_object_or_404(Post, pk=pk, status=True)
        post.delete()
        return Response(
            {"detail": "item remove successfully"}, status=status.HTTP_204_NO_CONTENT
        )
"""


class PostModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    queryset = Post.objects.filter(status=True)
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = {
        "category": ["exact"],
        "author": ["exact", "in"]
        }
    search_fields = ["title", "content"]
    ordering_fields = ["published_date"]

    serializer_class = PostSerializer
    pagination_class = DefualtPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user.profile.user)


"""    def get_serializer_class(self):
        if self.action == "list":
            return PostListSerializer

        if self.action == "retrieve":
            return PostDetailSerializer

        return PostSerializer"""


""" def perform_update(self, serializer):
        serializer.save(author=self.request.user.profile)
"""


class CategoryModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
