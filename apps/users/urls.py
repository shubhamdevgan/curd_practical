from unicodedata import name
from django.urls import path, include
from .views import SignUpUserView, UserDetail, UserDetailFillUpView, ChangePasswordView
from .viewsets import SignUpViewSet, UpdateProfileViewSet, CustomAuthToken, LogoutViewSet, DeleteUserViewSet


urlpatterns = [
    path('sign_up/', SignUpUserView.as_view(), name='sign-up'),
    path('user_detail/', UserDetail.as_view(), name='user_detail'),
    path('update/', UserDetailFillUpView.as_view(), name='update_view'),
    path('change_password/',
         ChangePasswordView.as_view(), name='change_password_view'),
    path('register_api/', SignUpViewSet.as_view(), name='register_api'),
    path('update_profile/', UpdateProfileViewSet.as_view(),
         name='update_profile_api'),
    path('update_profile/', UpdateProfileViewSet.as_view(),
         name='update_profile_api'),
    path('login_api/', CustomAuthToken.as_view(), name='login-api'),
    path('logout_api/', LogoutViewSet.as_view(), name='logout-api'),
    path('delete_api/', DeleteUserViewSet.as_view(), name='delete-api'),
]
