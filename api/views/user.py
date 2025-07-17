from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.tokens import RefreshToken
from api.serializers.user import UserSerializer


class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HomeView(APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request):
        content = {
            'message': 'Welcome to the JWT  Authentication page using React Js and Django!'}
        return Response(content)


class LogoutView(APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class UserInfoView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        user = request.user
        data = {
            'name': user.name,
            'email': user.email,
            'search_plan': user.search_plan,
            'search_count': user.search_count,
            'progress_count': user.progress_count,
            'max_searches': user.max_searches(),
        }
        return Response(data)


class UpdateSearchPlanView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        new_plan = request.data.get('suscription')
        if new_plan not in ['standard', 'business', 'premium']:
            return Response({'error': 'Invalid search plan'}, status=400)

        user = request.user
        user.search_plan = new_plan
        user.searches_allowed = user.max_searches()
        user.search_count = 0
        user.progress_count = 0
        user.save()

        return Response({'message': 'Search plan updated successfully', 'new_searches_allowed': user.searches_allowed, 'current_search_count': user.search_count}, status=200)


class IncrementSearchCountView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = request.user
        user.search_count += 1
        user.progress_count = (user.search_count / user.searches_allowed) * 100
        user.save()
        return Response({'new_search_count': user.search_count, 'new_progress_count': user.progress_count})
