from rest_framework import serializers
from .models import ChatSession, ChatMessage, Profile
import jdatetime
from django.contrib.auth.models import User


class ChatMessageSerializer(serializers.ModelSerializer):
    jalali_created_at = serializers.SerializerMethodField()

    class Meta:
        model = ChatMessage
        fields = ["id", "role", "content", "jalali_created_at"]

    def get_jalali_created_at(self, obj):
        return jdatetime.datetime.fromgregorian(datetime=obj.created_at).strftime(
            "%Y/%m/%d - %H:%M"
        )


class ProfileSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ["image"]


class ChatSessionSerializer(serializers.ModelSerializer):
    messages = ChatMessageSerializer(many=True, read_only=True)

    class Meta:
        model = ChatSession
        fields = ["id", "title", "started_at", "messages"]


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # Hide password in output

    class Meta:
        model = User
        fields = ("username", "email", "password")

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
        )
        return user
