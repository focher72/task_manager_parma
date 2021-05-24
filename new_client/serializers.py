from new_client.models import New_client
from rest_framework import serializers


class NewClientSerializer(serializers.ModelSerializer):
    """Форма для добавления/просмотра желающих на подключение"""
    class Meta:
        model = New_client
        fields = "__all__"
        read_only_fields = ('create_date', 'create_user',)
