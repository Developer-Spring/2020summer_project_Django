# Generated by Django 3.0.7 on 2020-07-06 08:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trial', '0008_auto_20200706_0803'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='InvestorType',
        ),
    ]
