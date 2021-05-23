from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, \
    TokenRefreshView
from .views import UserCreateView, UserRetriveUpdateView

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='auth_token'),
    path('login/refresh/', TokenRefreshView.as_view(),
         name='auth_token_refresh'),
    path('signup/', UserCreateView.as_view(), name='create_user'),
    path('profile/', UserRetriveUpdateView.as_view(), name='user_profile'),
    # path('profile/update_password/', update_password, name='update_password'),
    # path('profile/update_email/', update_email, name='update_password')
]
