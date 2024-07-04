from django_filters.rest_framework import DjangoFilterBackend
from rest_framework_json_api.views import ModelViewSet
from rest_framework_json_api.pagination import JsonApiPageNumberPagination
from rest_framework.filters import OrderingFilter

from wallet.models import Wallet, Transaction
from wallet.serializers import WalletSerializer, TransactionSerializer


class WalletViewSet(ModelViewSet):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer
    pagination_class = JsonApiPageNumberPagination
    filter_backends = (OrderingFilter, DjangoFilterBackend)
    ordering_fields = "__all__"
    filterset_fields = ("label",)


class TransactionViewSet(ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    pagination_class = JsonApiPageNumberPagination
    filter_backends = (OrderingFilter, DjangoFilterBackend)
    ordering_fields = "__all__"
    filterset_fields = ("wallet", "txid")
