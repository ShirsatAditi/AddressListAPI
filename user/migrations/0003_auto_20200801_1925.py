# Generated by Django 3.0.8 on 2020-08-01 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20200801_1301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='address_line1',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='address',
            name='city',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='address',
            name='pin_code',
            field=models.IntegerField(),
        ),
    ]
