from django.contrib import admin
from .models import ChangeLog


@admin.register(ChangeLog)
class ChangeLogAdmin(admin.ModelAdmin):
    list_display = ('changed', 'action_on_model', 'user', 'data',
                    'ipaddress',)
    readonly_fields = ('user', )
    list_filter = ('model', 'action_on_model',)
