from django.urls import path, include
from rest_framework.routers import DefaultRouter
from pod.apps.accounts.api.v1.views import AccountViewSet

router = DefaultRouter()
router.register(r'accounts', AccountViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
