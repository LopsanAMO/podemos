from django.contrib import admin
from pod.apps.groups.models import Group, Members


admin.site.register(Group)
admin.site.register(Members)
