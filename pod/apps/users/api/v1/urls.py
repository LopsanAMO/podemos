from django.urls import path, include
from rest_framework.routers import DefaultRouter
from pod.apps.users.api.v1.views import ClientListViewSet, UserCreateViewSet, CreateClientViewSet

router = DefaultRouter()
router.register(r'clients', ClientListViewSet)
router.register(r'client', CreateClientViewSet)
router.register(r'users', UserCreateViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
