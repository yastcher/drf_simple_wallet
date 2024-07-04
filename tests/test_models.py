from django.test import TestCase

from wallet.models import Wallet, Transaction


class TransactionTestCase(TestCase):
    def setUp(self):
        wallet1 = Wallet.objects.create(label="Wallet 1")
        wallet2 = Wallet.objects.create(label="Wallet 2")
        Transaction.objects.create(wallet=wallet1, txid="tx1", amount=50)
        Transaction.objects.create(wallet=wallet2, txid="tx2", amount=100)

    def test_transaction_amount(self):
        tx1 = Transaction.objects.get(txid="tx1")
        tx2 = Transaction.objects.get(txid="tx2")
        self.assertEqual(tx1.amount, 50)
        self.assertEqual(tx2.amount, 100)
        wallet1 = Wallet.objects.get(label="Wallet 1")
        wallet2 = Wallet.objects.get(label="Wallet 2")
        self.assertEqual(wallet1.balance, 50)
        self.assertEqual(wallet2.balance, 100)

    def test_delete_transaction(self):
        tx1 = Transaction.objects.get(txid="tx1")
        tx1.delete()
        wallet1 = Wallet.objects.get(label="Wallet 1")
        self.assertEqual(wallet1.balance, 0)
