from django.urls import path, include
from rest_framework.routers import DefaultRouter
from pod.apps.groups.api.v1.views import GroupMembersListViewSet, GroupAccountListViewSet, GroupViewSet,\
    GroupMemeberAPIView

router = DefaultRouter()
router.register(r'members', GroupMembersListViewSet)
router.register(r'detail', GroupAccountListViewSet)
router.register(r'group', GroupViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('groups/<str:group_id>', GroupMemeberAPIView.as_view())
]
