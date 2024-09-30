from django.urls import path
from .views import RegisterView, LoginView, UserViewSet

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('follow/<int:pk>/',
         UserViewSet.as_view({'post': 'follow_user'}), name='follow_user'),
    path('unfollow/<int:pk>/',
         UserViewSet.as_view({'post': 'unfollow_user'}), name='unfollow_user'),
]
