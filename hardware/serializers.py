from hardware import models
from rest_framework import serializers


class ActiveHardwareSerializer(serializers.ModelSerializer):
    """список активного оборудования"""
    class Meta:
        model = models.Active_hardware
        fields = "__all__"


class ActiveHardwarePortsSerializer(serializers.ModelSerializer):
    """список активного оборудования и порты на нем"""
    adress = serializers.StringRelatedField()
    count_ports = serializers.SerializerMethodField('get_count_ports')

    def get_count_ports(self, obj):
        return obj.hardware_ports.count()

    class Meta:
        model = models.Active_hardware
        fields = "__all__"


class ActiveHardwareHistorySerializer(serializers.ModelSerializer):
    """история активного оборудования"""
    history_user = serializers.StringRelatedField()
    adress = serializers.StringRelatedField()

    class Meta:
        model = models.Active_hardware_history
        fields = (
            'id',
            'history_user',
            'history_date',
            'name_hardware',
            'serial_num',
            'adress',
            'ip_adress',
            'mac_adress',
            'revision',
            'history_change_reason',
        )


class HardwareAdressSerializer(serializers.ModelSerializer):
    """Адреса оборудования и их точка"""
    class Meta:
        model = models.Hardware_adress
        fields = "__all__"


class PortsSerializer(serializers.ModelSerializer):
    """Полный список статусов"""

    class Meta:
        model = models.Hardware_ports
        # fields = "__all__"
        exclude = ('create_user', 'create_date',)
        read_only_fields = ('create_user', 'create_date',)


class PortsVlanSerializer(serializers.ModelSerializer):
    """Полный список статусов"""
    port_vlan = serializers.StringRelatedField(many=True)

    class Meta:
        model = models.Hardware_ports
        # fields = "__all__"
        exclude = ('create_user', 'create_date', 'hardware',)
        read_only_fields = ('create_user', 'create_date',)


class HardwarePortsReadSerializer(serializers.ModelSerializer):
    """Порты на оборудовании, только для чтения (для VlanReadSerializer)"""
    hardware = serializers.StringRelatedField(many=False)
    client_service = serializers.StringRelatedField(many=False)

    class Meta:
        model = models.Hardware_ports
        fields = ("hardware", "port_number", "client_service",)
        read_only_fields = ('create_user', 'create_date',)


class VlanSerializer(serializers.ModelSerializer):
    """Vlanы"""
    class Meta:
        model = models.Vlan
        fields = "__all__"


class VlanPortsSerializer(serializers.ModelSerializer):
    """Vlanы только на чтение"""
    count_ports = serializers.SerializerMethodField('get_count_ports')

    def get_count_ports(self, obj):
        return obj.vlan_ports.count()

    class Meta:
        model = models.Vlan
        fields = ("id", "vlan_name", "comment", "count_ports",)


class HardwareConnectionsSerializer(serializers.ModelSerializer):
    """список статусов конкретной заявки"""
    class Meta:
        model = models.Hardware_connections
        fields = "__all__"
        read_only_fields = ('create_user', 'create_date',)
