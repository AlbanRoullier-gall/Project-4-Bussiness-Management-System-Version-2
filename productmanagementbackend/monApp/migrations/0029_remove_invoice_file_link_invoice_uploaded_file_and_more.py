# Generated by Django 4.2.6 on 2024-04-05 15:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('monApp', '0028_invoice_file_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='file_link',
        ),
        migrations.AddField(
            model_name='invoice',
            name='uploaded_file',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='monApp.uploadedfile'),
        ),
        migrations.AlterField(
            model_name='uploadedfile',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
