from django.core.exceptions import ValidationError
from django.db.models import Sum, F
from django.db.models.signals import pre_save, post_save, post_delete
from django.dispatch import receiver

from wallet.models import Transaction


def update_balance(wallet):
    balance = wallet.transactions.aggregate(total=Sum(F("amount")))["total"] or 0
    wallet.balance = balance
    wallet.save(update_fields=["balance"])


@receiver(pre_save, sender=Transaction)
def validate_transaction(sender, instance, **kwargs):
    if instance.wallet.balance + instance.amount < 0:
        raise ValidationError("Wallet balance should NEVER be negative")


@receiver(post_save, sender=Transaction)
def update_wallet_balance_on_save(sender, instance, created, **kwargs):
    if created:
        update_balance(instance.wallet)


@receiver(post_delete, sender=Transaction)
def update_wallet_balance_on_delete(sender, instance, **kwargs):
    update_balance(instance.wallet)
