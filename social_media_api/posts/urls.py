from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet
from .views import FeedView
from .views import LikePostView, UnlikePostView

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('feed/', FeedView.as_view(), name='user_feed'),
    path('post/<int:pk>/like/', LikePostView.as_view(), name='like-post'),
    path('post/<int:pk>/unlike/', UnlikePostView.as_view(), name='unlike-post'),
]