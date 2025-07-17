from rest_framework.permissions import IsAuthenticated
from api.BackendClient.payment import PaymentApiClient, NotificationApiClient
from django.conf import settings
from rest_framework import viewsets
from rest_framework.response import Response
from core.models import User
from api.serializers.user import UserSerializer
from rest_framework.views import APIView
from django.core.cache import cache

access_token = settings.SECRET_ACCESS_KEY


class PaymentApiView(viewsets.ViewSet):
    # permission_classes = (IsAuthenticated, )

    def get_payment_client(self, request):
        client = PaymentApiClient(
            access_token=access_token,
            data=request.data
        )
        return client

    def create_preference(self, request):
        payment_client = self.get_payment_client(request)
        payment = payment_client.create_preference()

        return Response(payment)


class CurrentPlan(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, )

    def cache(self, request):
        email = request.data.get('email')
        plan = request.data.get('plan')
        cache.set(email, plan, timeout=720)
        return Response({'email': email, 'plan': plan})

    def send_plan(self, request):
        email = request.data.get('email')
        plan = cache.get(email)
        return Response({'plan': plan})
