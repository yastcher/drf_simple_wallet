import os

import django.db.models.deletion
from django.contrib.auth import get_user_model
from django.db import migrations, models


def create_superuser(apps, schema_editor):
    user_mdl = get_user_model()
    username = os.environ.get("DJANGO_SUPERUSER_USERNAME")
    email = os.environ.get("DJANGO_SUPERUSER_EMAIL")
    password = os.environ.get("DJANGO_SUPERUSER_PASSWORD")
    if not user_mdl.objects.filter(username=username).exists():
        user_mdl.objects.create_superuser(
            username=username,
            email=email,
            password=password,
        )


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.RunPython(create_superuser),
        migrations.CreateModel(
            name="Wallet",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("label", models.CharField(max_length=100)),
                (
                    "balance",
                    models.DecimalField(decimal_places=18, default=0, max_digits=36),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Transaction",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("txid", models.CharField(max_length=100, unique=True)),
                ("amount", models.DecimalField(decimal_places=18, max_digits=36)),
                (
                    "wallet",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="transactions",
                        to="wallet.wallet",
                    ),
                ),
            ],
        ),
        migrations.AddIndex(
            model_name="transaction",
            index=models.Index(fields=["amount"], name="wallet_tran_amount_a87b0b_idx"),
        ),
        migrations.AddIndex(
            model_name="wallet",
            index=models.Index(fields=["label"], name="wallet_wall_label_cb7ce7_idx"),
        ),
        migrations.AddIndex(
            model_name="wallet",
            index=models.Index(
                fields=["balance"], name="wallet_wall_balance_1ea64d_idx"
            ),
        ),
    ]
