from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import status
# Importa la función get_user_model para obtener el modelo de usuario personalizado
from django.contrib.auth import get_user_model
from api.serializers.user import UserSerializer
User = get_user_model()  # Obtén el modelo de usuario personalizado


class UserDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            user_id = request.user.id
            user = User.objects.get(id=user_id)
            user_data = {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'name': user.name,
                'surname': user.surname,
                'phone': user.phone,
                'country': user.country,
                'city': user.city,
                'address': user.address,
                'gender': user.gender,
                'date_of_birth': user.date_of_birth,
                'password': user.password
            }
            return Response(user_data)
        except User.DoesNotExist:
            return Response({'error': 'Usuario no encontrado'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request):
        user_id = request.user.id
        try:
            user = User.objects.get(id=user_id)
            serializer = UserSerializer(user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response({'error': 'Usuario no encontrado'}, status=status.HTTP_404_NOT_FOUND)


class UserEmailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        try:
            user_id = request.user.id
            user = User.objects.get(id=user_id)
            user_data = {
                'id': user.id,
                'email': user.email,
            }
            return Response(user_data)
        except User.DoesNotExist:
            return Response({'error': 'Usuario no encontrado'}, status=status.HTTP_404_NOT_FOUND)
