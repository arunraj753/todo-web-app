from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
import base64

from .serializers import UserRegisterSerializer, ProfileSerializer
from .models import User


class UserRegistrationView(APIView):

    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            print(user)
            response_dict = {"message": "User Registration Success !"}
            return Response(response_dict, status=201)


@api_view(['POST'])
def test(request):
    return Response('Working!', status=200)

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
        'first_name':user.first_name
    }


class LoginView(APIView):

    permission_classes = (AllowAny,)

    def post(self, request):
        username    = request.data.get('username', None)
        password = request.data.get('password', None)
        if (username and password):
            if not '@' in username:
                if not username.isdigit():
                    return Response({'message': 'Please provide a valid email/mobile'}, status=404)
                mobile = int(username)
                try:
                    user = User.objects.get(mobile=mobile)
                    username = user.email
                except:
                    return Response({'message': 'Please provide a valid email/mobile'}, status=404)
            user = authenticate(email=username, password=password)
            if user:
                tokens = get_tokens_for_user(user)
                return Response(tokens, status=200)
        return Response({'message': 'Invalid credentials'}, status=401)

class Profile(APIView):

    def get(self,request):
        serializer = ProfileSerializer(request.user)
        return Response(serializer.data, status=200)
       