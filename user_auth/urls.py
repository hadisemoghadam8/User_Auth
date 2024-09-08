# to add the URLs for the login, register, and test views 
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('authenticate/', include('authenticate.urls')),
    path('token/', include('token.urls')),
]