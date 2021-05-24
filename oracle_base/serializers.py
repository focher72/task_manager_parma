from oracle_base.models import Client_lists, Client_shpd_info
from rest_framework import serializers


class ClientListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client_lists
        fields = '__all__'


class ClientShpdInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client_shpd_info
        fields = '__all__'
