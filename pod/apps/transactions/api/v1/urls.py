from django.urls import path, include
from pod.apps.transactions.api.v1.views import TransactionCreateViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'transaction', TransactionCreateViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
