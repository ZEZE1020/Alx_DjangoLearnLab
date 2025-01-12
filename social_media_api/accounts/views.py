from django.shortcuts import render
from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .serializers import CustomUserSerializer, TokenSerializer
from django.http import HttpResponse
from django_restframework.views import APIView


def home(request):
    return HttpResponse("Welcome to the Social Media API!!")

# Create your views here.
User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        Token.objects.create(user=user)

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request}) 
        serializer.is_valid(raise_exception=True) 
        user = serializer.validated_data['user'] 
        token, created = Token.objects.get_or_create(user=user) 
        return Response({'token': token.key, 'user_id': user.id, 'email': user.email})



class UserListView(generics.GenericAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ProfileView(APIView):
    permission_classes = [IsAuthenticated]
    permissions.IsAuthenticated

    def get(self, request, *args, **kwargs):
        user = request.user
        return Response({
            'username': user.username,
            'email': user.email
        })


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def follow_user(request, user_id):
    try:
        user_to_follow = User.objects.get(id=user_id)
        request.user.following.add(user_to_follow)
        return Response({'status': 'success', 'message': 'You are now following {}'.format(user_to_follow.username)}, status=status.HTTP_200_OK)
    except User.DoesNotExist:
        return Response({'status': 'error', 'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def unfollow_user(request, user_id):
    try:
        user_to_unfollow = User.objects.get(id=user_id)
        request.user.following.remove(user_to_unfollow)
        return Response({'status': 'success', 'message': 'You have unfollowed {}'.format(user_to_unfollow.username)}, status=status.HTTP_200_OK)
    except User.DoesNotExist:
        return Response({'status': 'error', 'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
