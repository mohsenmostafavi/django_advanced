from rest_framework import serializers
from blog.models import Category, Post

# Example of Serializer fields
"""class PostSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=250)"""


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            "id",
            "name",
        ]


class PostSerializer(serializers.ModelSerializer):
    snippet = serializers.ReadOnlyField(source="get_snippet")
    relative_url = serializers.URLField(source="get_absolute_url", read_only=True)
    absolute_url = serializers.SerializerMethodField()
    category = serializers.SlugRelatedField(
        many=False, slug_field="name", queryset=Category.objects.all()
    )

    class Meta:
        model = Post
        fields = [
            "id",
            "author",
            "title",
            "content",
            "category",
            "image",
            "status",
            "snippet",
            "relative_url",
            "absolute_url",
            "published_date",
        ]
        read_only_fields = [
            "author",
        ]

    def get_absolute_url(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.get_absolute_url())

    def to_representation(self, instance):
        rep = super().to_representation(instance)

        request = self.context.get("request")
        view = self.context.get("view")
        action = getattr(view, "action", None)

        if action == "retrieve":
            # فیلدهای غیرضروری در post-detail
            rep.pop("snippet", None)
            rep.pop("relative_url", None)
            rep.pop("absolute_url", None)

        elif action == "list":
            # در post-list فقط relative_url حذف شود
            rep.pop("relative_url", None)

        rep["category"] = CategorySerializer(
            instance.category, context={"request": request}
        ).data

        return rep


""" def create(self, validated_data):
        '''get author field value from current user'''

        request = self.context.get("request")

        if request is None or not request.user.is_authenticated:
            raise serializers.ValidationError("کاربر احراز هویت‌شده یافت نشد.")

        validated_data["author"] = request.user.profile
        return Post.objects.create(**validated_data)"""


""" def to_representation(self, instance):
        request = self.context.get("request")
        rep = super().to_representation(instance)

        if request.parser_context.get("kwargs").get("pk"):
            rep.pop("snippet", None)
            rep.pop("relative_url", None)
            rep.pop("absolute_url", None)
        else:
            rep.pop("relative_url", None)
        rep["category"] = CategorySerializer(instance.category).data
        return rep"""


'''class PostDetailSerializer(serializers.ModelSerializer):
    """Special serializer for post-detail end-point"""

    snippet = serializers.ReadOnlyField(source="get_snippet")
    relative_url = serializers.URLField(source="get_absolute_url", read_only=True)
    absolute_url = serializers.SerializerMethodField()

    category = CategorySerializer(read_only=True)

    class Meta:
        model = Post
        fields = [
            "id",
            "author",
            "title",
            "content",
            "category",
            "image",
            "status",
            "snippet",
            "relative_url",
            "absolute_url",
            "published_date",
        ]
        read_only_fields = [
            "author",
        ]

    def get_absolute_url(self, obj):
        request = self.context.get("request")

        if request:
            return request.build_absolute_uri(obj.get_absolute_url())
        return obj.get_absolute_url()


class PostListSerializer(serializers.ModelSerializer):
    """Special serializer for post-list end-point"""

    category = CategorySerializer(read_only=True)

    class Meta:
        model = Post
        fields = [
            "id",
            "title",
            "category",
            "image",
            "status",
            "published_date",
        ]'''
