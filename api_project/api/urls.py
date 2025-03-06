from django.urls import path,include
from .views import BookList
from rest_framework import routers
from .views import BookViewSet
from .views import ListUsers
from .views import CustomAuthToken

router=routers.DefaultRouter()

router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    path('books/',BookList.as_view(), name='book-list'),
    path('', include(router.urls)),
    path('users/',ListUsers.as_view(), name = 'api-token-authentication'),
    path('token/auth/',CustomAuthToken.as_view())
]
