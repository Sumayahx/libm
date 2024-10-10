from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import UserRegistrationSerializer

class RegisterView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            login(request, user)

            return Response({"Registration Successful. User logged in."}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return Response({"Log in successful."}, status=status.HTTP_200_OK)
        else:
            return Response({'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

#@method_decorator(csrf_exempt, name='dispatch')
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        logout(request)
        return Response({"Successfully logged out."}, status=status.HTTP_200_OK)





# @api_view(['POST'])
# def register_user(request):
#     if request.method == 'POST':
#         serializer = UserRegistrationSerializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.save()

#             token, created = Token.objects.get_or_create(user=user)
#             return Response({
#                 'message': 'User created successfully',
#                 'token': token.key 
#             }, status=status.HTTP_201_CREATED)
        
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# @api_view(['POST'])
# #@permission_classes([IsAuthenticated])
# def logout_view(request):
#     if request.method == 'POST':
#         if request.user.is_authenticated:
#             request.user.auth_token.delete()
#             return Response(status=status.HTTP_200_OK)
#         else:
#             return Response(status=status.HTTP_401_UNAUTHORIZED)
