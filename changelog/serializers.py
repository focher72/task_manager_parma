from changelog import models
from rest_framework import serializers


class ChangeLogSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ChangeLog
        fields = '__all__'
