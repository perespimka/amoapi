# Generated by Django 3.0.3 on 2020-03-10 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monyzeapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='pass_reset_token',
            field=models.CharField(blank=True, max_length=45, null=True),
        ),
    ]