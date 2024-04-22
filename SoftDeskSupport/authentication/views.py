from django.contrib.auth import authenticate, login, logout

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework import status

from django.utils.decorators import method_decorator

from rest_framework_simplejwt.tokens import RefreshToken

from .models import User

from .serializers import UserSerializer

# Create your views here.


class AuthenticationViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    @action(detail=False, methods=['post'])
    def user_login(self, request):
        if request.user.is_authenticated:
            # L'utilisateur est déjà authentifié, vous pouvez renvoyer un message ou une réponse appropriée
            return Response({'message': 'Vous êtes déjà connecté.'}, status=status.HTTP_200_OK)
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(request=request, username= username, password = password)

        if user is not None: 
            login(request, user)

            refresh = RefreshToken.for_user(user)

            serializer = UserSerializer(user)

            return Response({
                "user":serializer.data,
                "refresh_token": str(refresh),
                "access_token": str(refresh.access_token),
            }, status=status.HTTP_200_OK)
        else:
            return Response({"error": 'Identifiant invalides.'}, status=status.HTTP_401_UNAUTHORIZED)
    @action(detail=False, methods=['post'])
    def user_logout(self, request):
        logout(request=request)

        return Response({
            "message": 'Deconnexion réussis'
        }, status=status.HTTP_200_OK)

    
