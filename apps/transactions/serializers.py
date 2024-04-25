from rest_framework import serializers
from apps.users.models import Users
from apps.transactions.models import GeekCoinTransaction

class TransferSerializers(serializers.ModelSerializer):
    class Meta:
        model = GeekCoinTransaction
        fields = ('sender', 'recipient', 'amount', 'date')

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        sender_id = representation.get('sender')
        recipient_id = representation.get('recipient')

        if sender_id:
            sender = Users.objects.get(id=sender_id)
            representation['sender'] = sender.username

        if recipient_id:
            recipient = Users.objects.get(id=recipient_id)
            representation['recipient'] = recipient.username

        return representation

    def create(self, validated_data):
        sender_id = validated_data.pop('sender', None)
        recipient_id = validated_data.pop('recipient', None)

        transfer = GeekCoinTransaction.objects.create(**validated_data)

        if sender_id:
            sender = Users.objects.get(id=sender_id)
            transfer.sender = sender

        if recipient_id:
            recipient = Users.objects.get(id=recipient_id)
            transfer.recipient = recipient

        transfer.save()

        return transfer
