from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers
from rest_framework import viewsets
from profiles_api import models
from rest_framework.authentication import TokenAuthentication
from profiles_api import permissions
from rest_framework import filters


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


class HelloViewSet(viewsets.ViewSet):
    """Test API VIEWSETS"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a Hello Message"""
        a_viewset = [
        'Uses Action (list, create, retrieve, update, partial_update)',
        'Automatically maps to urls using routers',
        'provides more functionality with less code',
        ]

        return Response({'message':'Hello!', 'a_viewset':a_viewset})

    def create(self, request):
        """Create a New Hello Message"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Handle Getting an Objet By its ID"""
        return Response({'http_method':'GET'})

    def update(self, request, pk=None):
        """Handle Updating an object """
        return Response({'http_method':'PUT'})

    def partial_update(self, request, pk=None):
        """Handle updating part of an object"""
        return Response({'http_method':'PATCH'})

    def destroy(self, request,pk=None):
        """Handle Removing an Object"""
        return Response({'http_method':'Delete'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permissions_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','email',)
