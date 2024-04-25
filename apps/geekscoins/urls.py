from rest_framework.routers import DefaultRouter
from django.urls import path

from apps.geekscoins.views import BalanceViewSet

router = DefaultRouter()
router.register('geekcoinbalance', BalanceViewSet, 'api_geekcoinbalance')


urlpatterns = router.urls
