import os
from dotenv import load_dotenv
from rest_framework import viewsets
from rest_framework.response import Response
from api.BackendClient.tiktok import TiktTokApiClient
from rest_framework.permissions import IsAuthenticated

load_dotenv()
TIKTOK_KEY = os.getenv("TIKTOK_KEY")
TIKTOK_SECRET_KEY = os.getenv("TIKTOK_SECRET_KEY")

class TiktTokApiView(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, )
    def get_tiktok_client(self):

        return TiktTokApiClient(
            tiktok_key = TIKTOK_KEY,
            tiktok_secret_key = TIKTOK_SECRET_KEY
        )

    def video_interest(self, request, id:str):
        tiktok_client = self.get_tiktok_client()
        response = tiktok_client.get_video_tiktok(id)

        return Response(response.json()['data']['ads'])