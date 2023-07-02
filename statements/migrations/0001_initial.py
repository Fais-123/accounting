# Generated by Django 4.2.2 on 2023-06-13 08:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Accounts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('account_type', models.CharField(max_length=100)),
                ('balance', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('description', models.CharField(max_length=100)),
                ('amount', models.IntegerField()),
                ('account_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='statements.accounts')),
            ],
        ),
        migrations.CreateModel(
            name='Entries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('description', models.CharField(max_length=100)),
                ('debit_amount', models.IntegerField()),
                ('credit_amount', models.IntegerField()),
                ('credit_account_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='credit_ledger_entries', to='statements.accounts')),
                ('debit_account_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='debit_ledger_entries', to='statements.accounts')),
            ],
        ),
    ]