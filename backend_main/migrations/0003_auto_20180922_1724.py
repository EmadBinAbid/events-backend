# Generated by Django 2.0.1 on 2018-09-22 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend_main', '0002_auto_20180919_1322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalorg',
            name='verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='org',
            name='verified',
            field=models.BooleanField(default=False),
        ),
    ]