# Generated by Django 4.2.6 on 2024-01-15 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monApp', '0015_alter_item_product_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='supplier_number',
            field=models.CharField(max_length=30),
        ),
    ]
