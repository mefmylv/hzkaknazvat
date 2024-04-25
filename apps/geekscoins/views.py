from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from apps.users.models import Users
from apps.geekscoins.serializers import BalanceSerializers



class BalanceViewSet(GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = Users.objects.all()
    serializer_class = BalanceSerializers
  

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Users.objects.filter(username=self.request.user)
        else:
            return Users.objects.none()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
