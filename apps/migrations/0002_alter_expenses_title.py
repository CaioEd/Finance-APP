# Generated by Django 5.1.6 on 2025-02-24 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expenses',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Expense Title'),
        ),
    ]
