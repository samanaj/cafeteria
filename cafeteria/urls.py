"""cafeteria URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, re_path, include
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
    path('admin/', admin.site.urls),
    # rest_framework token
    # path('api-auth/', include('rest_framework.urls')),
    #simple_ jwt
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    #apps local
    re_path('login', include(('apps.bases.urls', 'bases'), namespace= 'panel')),
    re_path('inv/', include(('apps.inv.urls', 'inv'), namespace= 'inv')),
    re_path('user/', include(('apps.usuarios.urls', 'usuarios'), namespace= 'user')),
    #importar routers
    re_path('', include('apps.usuarios.routers')),
]
