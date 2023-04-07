from rest_framework import serializers

from ..models import UsersPosts, Ad


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = '__all__'


class UsersPostsSerializer(serializers.ModelSerializer):
    content_type = serializers.SerializerMethodField()

    class Meta:
        model = UsersPosts
        fields = '__all__'

    def get_content_type(self, obj, *args, **kwargs):
        return obj.post_content_type.model


class AdSerializer(serializers.ModelSerializer):
    content_type = serializers.SerializerMethodField()

    class Meta:
        model = Ad
        fields = '__all__'

    def get_content_type(self, *args, **kwargs):
        return 'ad'

# class AchievementSerializer(serializers.ModelSerializer):
#     content_type = serializers.SerializerMethodField()
#
#     class Meta:
#         model = Achievement
#         fields = '__all__'
#
#     def get_content_type(self, *args, **kwargs):
#         return 'achievement'
#
#
# class NoteSerializer(serializers.ModelSerializer):
#     content_type = serializers.SerializerMethodField()
#
#     class Meta:
#         model = Note
#         fields = '__all__'
#
#     def get_content_type(self, *args, **kwargs):
#         return 'note'
#
#
