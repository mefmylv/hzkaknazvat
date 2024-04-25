from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.shortcuts import get_object_or_404
from django.db import transaction
from rest_framework import serializers

from apps.transactions.models import GeekCoinTransaction
from apps.transactions.serializers import TransferSerializers
from apps.users.models import Users
from apps.users.permissions import UserPermissons

class TransactionsAPIViews(GenericViewSet, 
                           mixins.ListModelMixin,
                           mixins.CreateModelMixin):
    queryset = GeekCoinTransaction.objects.all()
    serializer_class = TransferSerializers
    permission_classes = IsAuthenticated

    def get_permissions(self):
        if self.action in ('update', 'partial_update', 'destroy'):
            return (UserPermissons(), )
        return (AllowAny(), )
    
    def perform_create(self, serializer):
        try:
            sender = get_object_or_404(Users, username=str(serializer.validated_data['sender']))
            recipient = get_object_or_404(Users, username=str(serializer.validated_data['recipient']))
            amount = float(serializer.validated_data['amount'])

            if amount > float(sender.balance):
                raise serializers.ValidationError('Недостаточно средств для перевода')

            with transaction.atomic():
                sender.save()
                recipient.save()

                transfer = GeekCoinTransaction(sender=sender, recipient=recipient, amount=amount)
                transfer.save()

        except (Users.DoesNotExist, ValueError, serializers.ValidationError) as e:
            raise serializers.ValidationError({'detail': str(e)})



class TransactionHistoryAPIView(GenericViewSet,
                                mixins.ListModelMixin,
                                mixins.RetrieveModelMixin):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        user = request.user
        transactions = GeekCoinTransaction.objects.filter(sender=user) | GeekCoinTransaction.objects.filter(recipient=user)
        serializer = TransferSerializers(transactions, many=True)
        return Response(serializer.data)