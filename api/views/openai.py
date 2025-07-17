import os
from openai import OpenAI, OpenAIError
from dotenv import load_dotenv
from rest_framework import viewsets
from rest_framework.response import Response
from api.BackendClient.openai import OpenAIClient
from api.serializers.openai import OpenAISerializer
from rest_framework.permissions import IsAuthenticated

load_dotenv()
OPENAI_KEY = os.getenv("OPENAI_KEY")


class OpenAIApiView(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, )

    def get_openai_client(self):
        client = OpenAI(
            api_key=OPENAI_KEY
        )

        return client

    def get_api_openai_client(self):
        return OpenAIClient(
            openai_client=self.get_openai_client()
        )

    def recommend_video(self, request, id: str):
        get_openai_client = self.get_api_openai_client()
        try:
            response = get_openai_client.get_recommend(id)
            recommendation_text = response.choices[0].text.strip()
            serializer = OpenAISerializer(data={'prompt': recommendation_text})

            if serializer.is_valid():
                serialized_data = serializer.data
                return Response(serialized_data)
            else:
                return Response(serializer.errors, status=400)
        except OpenAIError as e:
            return Response({'error': str(e)}, status=500)

    def recommend_copy(self, request, id: str):
        get_openai_client = self.get_api_openai_client()
        try:
            response = get_openai_client.get_copy(id)
            recommendation_text = response.choices[0].text.strip()
            serializer = OpenAISerializer(data={'prompt': recommendation_text})

            if serializer.is_valid():
                serialized_data = serializer.data
                return Response(serialized_data)
            else:
                return Response(serializer.errors, status=400)
        except OpenAIError as e:
            return Response({'error': str(e)}, status=500)

    def recommend_landing(self, request, id: str):
        get_openai_client = self.get_api_openai_client()
        try:
            response = get_openai_client.get_landing(id)
            recommendation_text = response.choices[0].text.strip()
            serializer = OpenAISerializer(data={'prompt': recommendation_text})

            if serializer.is_valid():
                serialized_data = serializer.data
                return Response(serialized_data)
            else:
                return Response(serializer.errors, status=400)
        except OpenAIError as e:
            return Response({'error': str(e)}, status=500)
