# Generated by Django 4.2.6 on 2024-04-16 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monApp', '0032_alter_invoice_communication'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='total_amount_exc_vat',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='total_amount_vat',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
