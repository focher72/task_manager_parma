from task_manager import models
from rest_framework import serializers
from datetime import datetime


class TaskUserWorkSerializer(serializers.ModelSerializer):
    """список исполнителей заявки"""
    class Meta:
        model = models.Task_user_work
        fields = "__all__"
        read_only_fields = ('start_date', 'end_date', 'create_user', 'create_date',)


class TaskMessagesSerializer(serializers.ModelSerializer):
    """Комментарии от сотрудников к заявке"""
    class Meta:
        model = models.Task_messages
        fields = "__all__"
        read_only_fields = ('create_date', 'create_user')


class TaskSerializer(serializers.ModelSerializer):
    """список всех заявок"""
    class Meta:
        model = models.Task
        fields = "__all__"
        read_only_fields = ('create_user', 'create_date',)


class StatusSerializer(serializers.ModelSerializer):
    """Полный список статусов"""
    class Meta:
        model = models.Status
        fields = "__all__"


class TaskTypesSerializer(serializers.ModelSerializer):
    """Полный список статусов"""
    class Meta:
        model = models.Task_types
        fields = "__all__"


class TaskSourceSerializer(serializers.ModelSerializer):
    """Полный список статусов"""
    class Meta:
        model = models.Task_source
        fields = "__all__"


class TaskStatusSerializer(serializers.ModelSerializer):
    """список статусов конкретной заявки"""
    class Meta:
        model = models.Task_status
        fields = "__all__"
        read_only_fields = ('start_date', 'end_date', 'create_user', 'create_date',)


class TaskFullInfoSerializer(serializers.ModelSerializer):
    """Полная информация о заявке (для печати)"""
    type = serializers.SlugRelatedField(read_only=True, many=False,
                                        slug_field='task_name')
    source = serializers.StringRelatedField(read_only=True, many=False)
    create_user = serializers.StringRelatedField(many=False)
    client = serializers.StringRelatedField(many=False)
    current_status = serializers.SerializerMethodField()
    current_user = serializers.SerializerMethodField()
    close_date = serializers.SerializerMethodField()
    close_comment = serializers.SerializerMethodField()

    class Meta:
        model = models.Task
        fields = "__all__"

    def get_current_status(self, obj):
        """Последний статус заявки"""
        last_status = models.Task_status.objects.filter(
            task=obj.pk,
            end_date__gte=datetime.now()
        ).latest('start_date')
        return last_status.status.status_name

    def get_current_user(self, obj):
        """Исполнитель"""
        work_user = models.Task_user_work.objects.filter(
            task=obj.pk,
            end_date__gte=datetime.now()) \
            .order_by('-start_date').first()
        return work_user.user.username

    def get_close_date(self, obj):
        """Дата закрытия заявки"""
        try:
            close_date = models.Task_status.objects.get(
                task=obj.pk,
                status=models.Status.objects.get(status_name='Закрыта'),
                end_date__gte=datetime.now())
            return close_date.start_date
        except models.Task_status.DoesNotExist:
            return '--'

    def get_close_comment(self, obj):
        """Дата закрытия заявки"""
        try:
            close_comment = models.Task_status.objects.get(
                task=obj.pk,
                status=models.Status.objects.get(status_name='Закрыта'),
                end_date__gte=datetime.now())
            return close_comment.comment
        except models.Task_status.DoesNotExist:
            return '--'
