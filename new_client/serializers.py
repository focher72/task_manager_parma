from new_client.models import New_client, Client_adress
from rest_framework import serializers


class NewClientSerializer(serializers.ModelSerializer):
    """Форма для добавления/просмотра желающих на подключение"""
    class Meta:
        model = New_client
        fields = "__all__"
        read_only_fields = ('create_date', 'create_user',)


class ClientAdressSerializer(serializers.ModelSerializer):
    """Адреса желающих на подключение"""
    class Meta:
        model = Client_adress
        fields = "__all__"


class NewClientReadSerializer(serializers.ModelSerializer):
    """Форма для добавления/просмотра желающих на подключение"""
    adress = serializers.StringRelatedField()
    create_user = serializers.StringRelatedField()

    class Meta:
        model = New_client
        fields = "__all__"
        read_only_fields = ('create_date', 'create_user',)


class AdressAndCleintSerializer(serializers.ModelSerializer):
    """Адреса желающих на подключение"""
    client_adress = NewClientReadSerializer(many=True)

    class Meta:
        model = Client_adress
        fields = "__all__"
