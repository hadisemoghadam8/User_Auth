# to add the URLs for the login, register, and test views 
from django.urls import path, include

urlpatterns = [
    path('tokens/', include('tokens.urls')),
    path('authenticate/', include('authenticate.urls')),
    path('test/', include('tokens.urls')),  # for testing with access token
]