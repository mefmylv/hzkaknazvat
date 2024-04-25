from django.contrib import admin
from apps.transactions.models import GeekCoinTransaction
# Register your models here.
@admin.register(GeekCoinTransaction)
class TranserAdmin(admin.ModelAdmin):
    list_display = ['sender', 'recipient', 'amount', 'date']
    list_filter = ['sender', 'recipient', 'date']