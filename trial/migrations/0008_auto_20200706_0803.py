# Generated by Django 3.0.7 on 2020-07-06 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trial', '0007_auto_20200706_0723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='asset',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='document',
            name='debt',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='document',
            name='foreignassets',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='document',
            name='foreigndebt',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='document',
            name='investment',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='document',
            name='year_export',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='document',
            name='year_import',
            field=models.IntegerField(),
        ),
    ]