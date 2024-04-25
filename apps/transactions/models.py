from django.db import models
from django.core.validators import MaxValueValidator
from apps.users.models import Users


class GeekCoinTransaction(models.Model):
    sender = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='sender_transactions')
    recipient = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='recipient_transactions')
    amount = models.IntegerField(validators=[MaxValueValidator(4)])  
    date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        sender_balance = self.sender.balance
        recipient_wallet = self.recipient.wallet

        if sender_balance >= self.amount:
            if self.sender == self.recipient:
                raise ValueError("Нельзя отправить себе")
            else:
                self.sender.balance -= self.amount
                self.recipient.wallet += self.amount

            self.sender.save()
            self.recipient.save()
            super(GeekCoinTransaction, self).save(*args, **kwargs)
        else:
            raise ValueError("Insufficient funds for the transaction.")

    class Meta:
        verbose_name = 'Транзакция'
        verbose_name_plural = 'Транзакции'
