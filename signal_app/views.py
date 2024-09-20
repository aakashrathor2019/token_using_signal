from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework import status


class TokenView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        token, created = Token.objects.get_or_create(user=request.user)
        return Response({'token': token.key})


class UserCreateView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')

        if username and password:
            # Create user
            user = User.objects.create_user(username=username, password=password, email=email)
            
            # Token will be created automatically by the signal
            token, created = Token.objects.get_or_create(user=user)

            return Response({
                'message': 'User created successfully',
                'token': token.key
            }, status=status.HTTP_201_CREATED)
        return Response({'error': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)