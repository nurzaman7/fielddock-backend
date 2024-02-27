from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate

class AdminLoginView(APIView):
    def post(self, request, format=None):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user is not None and user.is_staff:
            # Include username in the response upon successful admin login
            return Response({'message': 'Admin login successful', 'username': user.username})
        else:
            return Response({'message': 'Invalid credentials or not an admin'}, status=status.HTTP_401_UNAUTHORIZED)

