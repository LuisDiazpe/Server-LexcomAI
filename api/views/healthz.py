from rest_framework.response import Response
from rest_framework.views import APIView


class TestView(APIView): 
    def get(self, request):     
        content = {
            'message': '200'
        }
        return Response(content)