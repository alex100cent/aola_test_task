from rest_framework import serializers

from ..models import UsersPosts, Ad, Post


class PostSerializer(serializers.ModelSerializer):
    post_type = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = '__all__'

    def get_post_type(self, obj, *args, **kwargs):
        return obj.POST_TYPE


class UsersPostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsersPosts
        fields = '__all__'


class AdSerializer(serializers.ModelSerializer):
    post_type = serializers.SerializerMethodField()

    class Meta:
        model = Ad
        fields = '__all__'

    def get_post_type(self, obj, *args, **kwargs):
        return obj.POST_TYPE
