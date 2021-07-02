from django.contrib import admin
from .models import Task, Status, Task_status, Task_types, Task_source, \
    Task_user_work, Task_messages


class TaskAdmin(admin.ModelAdmin):
    list_display = ('client', 'category', 'type', 'create_date',)
    list_display_links = ('client',)
    readonly_fields = ('create_user', 'create_date')
    search_fields = ('client',)
    list_filter = ('category', 'type', 'source',)


class TaskStatusAdmin(admin.ModelAdmin):
    list_display = ('task', 'status', 'start_date', 'end_date', 'comment',)
    list_display_links = ('task',)
    readonly_fields = ('create_user', 'start_date', 'end_date',)
    search_fields = ('task',)
    list_filter = ('status', 'task',)


class TaskUserWorkAdmin(admin.ModelAdmin):
    list_display = ('task', 'user', 'start_date', 'end_date', 'comment',)
    list_display_links = ('task',)
    readonly_fields = ('create_user', 'start_date', 'end_date',)
    search_fields = ('task',)
    list_filter = ('user', 'task',)


class TaskMessagesAdmin(admin.ModelAdmin):
    list_display = ('task', 'messages_text', 'create_date', 'create_user',)
    list_display_links = ('task',)
    readonly_fields = ('create_user', 'create_date')
    search_fields = ('task',)
    list_filter = ('task',)


class TaskTypesAdmin(admin.ModelAdmin):
    list_display = ('task_name', 'category',)
    search_fields = ('task_name',)
    list_filter = ('task_name',)


admin.site.register(Task, TaskAdmin)
admin.site.register(Task_status, TaskStatusAdmin)
admin.site.register(Task_user_work, TaskUserWorkAdmin)
admin.site.register(Task_messages, TaskMessagesAdmin)
admin.site.register(Task_types, TaskTypesAdmin)
admin.site.register(Task_source)
admin.site.register(Status)
