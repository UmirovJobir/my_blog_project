from django.urls import path
from .views import PostList, PostDetail, UserDetail, UserList, CommentList, CommentDetail


urlpatterns = [
    path('posts/', PostList.as_view()),
    path('posts/<str:pk>/', PostDetail.as_view()),

    path('users/', UserList.as_view()),
    path('users/<str:pk>/', UserDetail.as_view()),

    path('comments/', CommentList.as_view()),
    path('comments/<int:pk>/', CommentDetail.as_view()),
]