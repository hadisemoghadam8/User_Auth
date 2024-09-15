# to add the URLs for the login, register, and test views 
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html')),  # add this line
    path('tokens/', include('tokens.urls')),
    path('authenticate/', include('authenticate.urls')),
    path('test/', include('tokens.urls')),  # for testing with access token
]