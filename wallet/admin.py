from django.contrib import admin

from wallet.models import Wallet, Transaction


class WalletAdmin(admin.ModelAdmin):
    list_display = ("id", "label", "balance")
    readonly_fields = ("balance",)
    search_fields = ("label",)


class TransactionAdmin(admin.ModelAdmin):
    list_display = ("id", "wallet", "txid", "amount")
    search_fields = ("txid",)
    list_filter = ("wallet",)


admin.site.register(Wallet, WalletAdmin)
admin.site.register(Transaction, TransactionAdmin)
