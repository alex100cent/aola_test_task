from rest_framework import serializers

from ..models import User, UsersEvents, Achievement, Note, Ad


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UsersAchievementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsersEvents
        fields = '__all__'


class AchievementSerializer(serializers.ModelSerializer):
    content_type = serializers.SerializerMethodField()

    class Meta:
        model = Achievement
        fields = '__all__'

    def get_content_type(self, *args, **kwargs):
        return 'achievement'


class NoteSerializer(serializers.ModelSerializer):
    content_type = serializers.SerializerMethodField()

    class Meta:
        model = Note
        fields = '__all__'

    def get_content_type(self, *args, **kwargs):
        return 'note'


class AdSerializer(serializers.ModelSerializer):
    content_type = serializers.SerializerMethodField()

    class Meta:
        model = Ad
        fields = '__all__'

    def get_content_type(self, *args, **kwargs):
        return 'ad'
