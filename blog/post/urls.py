from django.contrib.auth import views as auth_views
from django.urls import path

from . import views
from . import api_views


urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('create/', views.PostCreateView.as_view(), name='post'),
    path('<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('update/<int:pk>/', views.PostUpdateView.as_view(), name='post_update'),
    path('delete/<int:pk>/', views.PostDeleteView.as_view(), name='post_delete'),

    # API
    path('api/like-toggle/', api_views.LikeToggleAPIView.as_view(), name='like-toggle'),
    path('api/post/<int:post_id>/comment/', api_views.CommentCreateAPI.as_view(), name='create_comment_api'),
]