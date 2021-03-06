# Generated by Django 3.0.7 on 2020-07-05 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('investor_type', models.DecimalField(decimal_places=1, max_digits=1)),
                ('asset', models.TextField()),
                ('debt', models.TextField()),
                ('foreignassets', models.TextField()),
                ('foreigndebt', models.TextField()),
                ('year_export', models.TextField()),
                ('year_import', models.TextField()),
                ('investment', models.TextField()),
            ],
        ),
    ]
