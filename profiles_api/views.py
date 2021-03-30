from rest_framework.views import APIView
from rest_framework.response import Response


class HelloAPIView(APIView):
    """TEST API VIEW"""

    def get(self, request, format=None):
        """ Returns a list of APIView Features"""
        an_APIView = [
        'Uses http method as function (get,post,patch,put,delete)',
        'Is similar to DJANGO View',
        'Gives you control over your application logic',
        'Is mapped manually to URLS',
        ]
        return response({'message' : "Hello",'an_APIView' : an_APIView})
