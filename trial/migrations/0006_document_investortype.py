# Generated by Django 3.0.7 on 2020-07-06 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trial', '0005_remove_document_investor_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='InvestorType',
            field=models.CharField(choices=[('1', '상장기업'), ('2', '비상장기업'), ('3', '개인사업자')], default='1', max_length=1),
        ),
    ]
