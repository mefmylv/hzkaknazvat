from rest_framework.routers import DefaultRouter
from apps.transactions.views import TransactionsAPIViews, TransactionHistoryAPIView
from django.urls import path

router = DefaultRouter()
router.register('transactions', TransactionsAPIViews, 'api_transactions')

urlpatterns = [
    path('history/', TransactionHistoryAPIView.as_view(actions={'get':'list'}), name='api_transfer_history'),
]

urlpatterns += router.urls