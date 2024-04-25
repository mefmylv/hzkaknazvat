from rest_framework import serializers
from apps.users.models import Users


class BalanceSerializers(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('username', 'balance', 'wallet')
