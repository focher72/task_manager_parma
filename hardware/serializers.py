from hardware import models
from rest_framework import serializers


class ActiveHardwareSerializer(serializers.ModelSerializer):
    """список активного оборудования"""
    class Meta:
        model = models.Active_hardware
        fields = "__all__"
        read_only_fields = ('create_user', 'create_date',)


class HardwareAdressSerializer(serializers.ModelSerializer):
    """Адреса оборудования и их точка"""
    class Meta:
        model = models.Hardware_adress
        fields = "__all__"


class ChangeReasonSerializer(serializers.ModelSerializer):
    """причина изменеия"""
    class Meta:
        model = models.Change_reason
        fields = "__all__"


class HardwareAdressHistorySerializer(serializers.ModelSerializer):
    """История изменения адреса оборудования"""
    class Meta:
        model = models.Hardware_adress_history
        fields = "__all__"
        read_only_fields = ('create_user', 'create_date',)


class VlanSerializer(serializers.ModelSerializer):
    """Vlanы"""
    class Meta:
        model = models.Vlan
        fields = "__all__"


class HardwarePortsSerializer(serializers.ModelSerializer):
    """Полный список статусов"""
    class Meta:
        model = models.Hardware_ports
        fields = "__all__"
        read_only_fields = ('create_user', 'create_date',)


class HardwareConnectionsSerializer(serializers.ModelSerializer):
    """список статусов конкретной заявки"""
    class Meta:
        model = models.Hardware_connections
        fields = "__all__"
        read_only_fields = ('create_user', 'create_date',)
