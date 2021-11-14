from rest_framework import serializers
from .models import User


class UserRegisterSerializer(serializers.ModelSerializer):

    # repeat_password = serializers.CharField(required=True)
    class Meta:
        model = User
        fields = "__all__"

    def save(self):
        print(self.validated_data)

        email       = self.validated_data["email"]
        mobile      = self.validated_data["mobile"]
        password    = self.validated_data["password"]
        first_name  = self.validated_data["first_name"]
        last_name   = self.validated_data.get("last_name", None)
        profile_pic = self.validated_data.get("profile_pic", None)
        user        = User.objects.create_user(
            email, mobile, password, first_name, last_name, profile_pic
        )
        return user

    def validate_mobile(self, value):
        if len(str(value)) == 10:
            return value
        raise serializers.ValidationError("Enter a valid 10 digit number")


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("email", "mobile", "first_name", "last_name", "profile_pic")
