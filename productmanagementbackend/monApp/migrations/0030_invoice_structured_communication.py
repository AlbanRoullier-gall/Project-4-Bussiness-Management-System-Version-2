# Generated by Django 4.2.6 on 2024-04-08 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monApp', '0029_remove_invoice_file_link_invoice_uploaded_file_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='structured_communication',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
    ]
