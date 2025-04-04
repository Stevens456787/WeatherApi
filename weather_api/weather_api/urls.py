"""
URL configuration for weather_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
#from users.views import UserViewSet, RegisterView, APIKeyView, LogoutView
from alerts.views import AlertViewSet  # Import AlertViewSet from the correct module
from locations.views import LocationViewSet
from weather.views import WeatherViewSet
#from users.views import LoginView
from visualization.views import VisualizationViewSet, chart_view  # Import VisualizationViewSet and chart_view from the correct module

router = DefaultRouter()
#router.register(r'users', UserViewSet)
router.register(r'weather', WeatherViewSet)
router.register(r'alerts', AlertViewSet)
router.register(r'locations', LocationViewSet, basename='location')
router.register(r'visualization', VisualizationViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    #path('api/register/', RegisterView.as_view(), name='register'),
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.authtoken')),
    #path('api/api-key/', APIKeyView.as_view(), name='api-key'),
    # path('chart/', chart_view, name='chart'),
]