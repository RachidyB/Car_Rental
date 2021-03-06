from knox import views as knox_views
from django.urls import path
from .views import LoginAPI, RegisterAPI, UserAPI, ChangePasswordView

urlpatterns = [
    path('register/', RegisterAPI.as_view(), name='register'),
    path('login/', LoginAPI.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('user/', UserAPI.as_view(), name='user'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
]
