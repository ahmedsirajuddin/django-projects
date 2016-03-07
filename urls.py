from django.conf.urls import url
from django.conf.urls import include
from CMSApp import views
from rest_framework import routers, serializers, viewsets

router = routers.DefaultRouter()
router.register(r'posts', views.PostViewSet, base_name='post')
