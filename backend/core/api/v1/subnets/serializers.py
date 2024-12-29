from rest_framework import serializers

from apps.subnets.models import Subnet


class SubnetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subnet
        fields = "__all__"
