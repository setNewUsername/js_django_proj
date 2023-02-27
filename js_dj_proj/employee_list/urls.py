from django.urls import include, path
from . import views
from rest_framework import routers
from .serializers import *

router = routers.DefaultRouter()

router.register(r'departments', views.DepartmentViewSet, basename='')
router.register(r'list', views.EmployeeVuewSet, basename='')

urlpatterns = [
    path('', include(router.urls)),
]