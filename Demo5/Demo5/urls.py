from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api import views
from rest_framework.authtoken.views import obtain_auth_token

"""we create default url which call student api"""
router = DefaultRouter()
router.register("studentapi",views.Studentapi, basename="student")

urlpatterns = [
    path('admin/', admin.site.urls),
    #"when we call curd url it will give as student url by which we can use our api"
    path("", include(router.urls)),
    path("auth/", include('rest_framework.urls',namespace='rest_framework')),
    path("gettoken/", obtain_auth_token),

    
] 