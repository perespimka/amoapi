# Generated by Django 3.0.3 on 2020-05-07 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amoapi', '0002_auto_20200506_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paintsleads',
            name='date_add',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
