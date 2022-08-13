from rest_framework.routers import DefaultRouter
from CQapp.views import CQuserView
from django.urls import path,include

router = DefaultRouter()
router.register('user',CQuserView)
urlpatterns = [
    path('',include(router.urls)),
]
