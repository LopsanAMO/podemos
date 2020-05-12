from django.urls import path, include
from pod.apps.users.api.v1 import urls as clienturls
from pod.apps.groups.api.v1 import urls as groupurls
from pod.apps.accounts.api.v1 import urls as accounturls
from pod.apps.transactions.api.v1 import urls as transactionurls


urlpatterns = [
    path('v1/users/', include(clienturls)),
    path('v1/groups/', include(groupurls)),
    path('v1/accounts/', include(accounturls)),
    path('v1/transactions/', include(transactionurls))
]