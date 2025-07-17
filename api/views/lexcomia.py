from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from api.BackendClient.lexcomia import LexComIA_Client
from api.serializers.lexcomai import LexcomFiveClassSerializer, LexcomBinaryClassSerializer
from rest_framework import viewsets


# class LexcomIA_ApiView(APIView):
class LexcomIA_ApiView(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, )

    def get_lexcom_client(self):
        client = LexComIA_Client()
        return client

    def probability_percentage(self, request):
        data = request.data
        lexcom_client = self.get_lexcom_client()
        response = lexcom_client.get_prediction_five_class(data)
        serializer = LexcomFiveClassSerializer(data={'very_good': response[0][0],
                                                     'good': response[0][1],
                                                     'normal': response[0][2],
                                                     'bad': response[0][3],
                                                     'very_bad': response[0][4]})
        if serializer.is_valid():
            serialized_data = serializer.data
            # print(serialized_data)
            return Response(serialized_data)
        else:
            return Response(serializer.errors, status=400)

    def probability_success(self, request):
        data = request.data
        lexcom_client = self.get_lexcom_client()
        response = lexcom_client.get_prediction_binary_class(data)
        serializer = LexcomBinaryClassSerializer(
            data={'success': response[0][0], 'failure': response[0][1]})

        if serializer.is_valid():
            serialized_data = serializer.data
            # print(serialized_data)
            return Response(serialized_data)
        else:
            return Response(serializer.errors, status=400)
