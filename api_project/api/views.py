from django.shortcuts import render
from rest_framework import generics,viewsets,authentication,permissions
from .models import Book
from .serializers import BookSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

# Create your views here.
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class=BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset=Book.objects.all().order_by('-author')
    serializer_class=BookSerializer

class ListUsers(APIView):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    def get(self,request,format=None):
        emails=[user.email for user in User.objects.all()]
        return Response(emails)

class CustomAuthToken(ObtainAuthToken):
    def post(self,request,*args,**kwargs):
        serializer=self.serializer_class(data=request.data,context={'request':request})
        serializer.is_valid(raise_exception=True)
        user=serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token':token.key,
            'user_id':user.pk,
            'email':user.email
        })
        