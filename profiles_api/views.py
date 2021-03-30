from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers


class HelloAPIView(APIView):
    """TEST API VIEW"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """ Returns a list of APIView Features"""
        an_APIView = [
        'Uses http method as function (get,post,patch,put,delete)',
        'Is similar to DJANGO View',
        'Gives you control over your application logic',
        'Is mapped manually to URLS',
        ]
        return Response({'message' : "Hello",'an_APIView' : an_APIView})

    def post(self, request):
        """Create a hello message with our name """
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'hello {name}'
            return Response({'message' : message})
        else:
            return Response(
            serializer.errors,
            status = status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """Handle Updating an Object"""
        return Response({'method' : 'PUT'})

    def patch(self, request, pk=None):
        """Handle Partial Update of Object"""
        return Response({'method': 'PATCH'})

    def delete(self,request,pk=None):
        """Deletes an Object"""
        return Response({'method':'delete'})
        
