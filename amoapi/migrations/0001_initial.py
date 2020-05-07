# Generated by Django 3.0.3 on 2020-05-06 11:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Leads',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amo_lead_id', models.IntegerField(unique=True)),
                ('user_id', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'leads',
            },
        ),
        migrations.CreateModel(
            name='Paints',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('product', models.CharField(max_length=45)),
                ('basis', models.CharField(max_length=45)),
                ('catalog', models.CharField(max_length=45)),
                ('code', models.CharField(max_length=45)),
                ('shine', models.CharField(max_length=45)),
                ('facture', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'paints',
            },
        ),
        migrations.CreateModel(
            name='PaintsLeads',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_add', models.CharField(blank=True, max_length=45, null=True)),
                ('temperature', models.CharField(blank=True, max_length=45, null=True)),
                ('applying', models.CharField(blank=True, max_length=45, null=True)),
                ('postforming', models.CharField(blank=True, max_length=45, null=True)),
                ('metallic', models.IntegerField(blank=True, null=True)),
                ('chameleon', models.IntegerField(blank=True, null=True)),
                ('antibacterial', models.IntegerField(blank=True, null=True)),
                ('antigraffiti', models.IntegerField(blank=True, null=True)),
                ('architect', models.IntegerField(blank=True, null=True)),
                ('zinc', models.IntegerField(blank=True, null=True)),
                ('client_sample', models.CharField(blank=True, max_length=45, null=True)),
                ('comment', models.CharField(blank=True, max_length=45, null=True)),
                ('potential_vol', models.IntegerField(blank=True, null=True)),
                ('kp_price', models.IntegerField(blank=True, null=True)),
                ('vol', models.FloatField(blank=True, null=True)),
                ('price', models.FloatField(blank=True, null=True)),
                ('delivery_date', models.CharField(blank=True, max_length=45, null=True)),
                ('delivery_terms', models.CharField(blank=True, max_length=45, null=True)),
                ('product_type', models.CharField(blank=True, max_length=45, null=True)),
                ('status', models.CharField(blank=True, max_length=45, null=True)),
                ('reason', models.CharField(blank=True, max_length=45, null=True)),
                ('surface', models.CharField(blank=True, max_length=45, null=True)),
                ('panels', models.IntegerField(blank=True, null=True)),
                ('powder', models.CharField(blank=True, max_length=10, null=True)),
                ('surface_type', models.CharField(blank=True, max_length=45, null=True)),
                ('surface_thin', models.CharField(blank=True, max_length=45, null=True)),
                ('ntime_applying', models.CharField(blank=True, max_length=45, null=True)),
                ('lead_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='amoapi.Leads')),
                ('paint_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='amoapi.Paints')),
            ],
            options={
                'db_table': 'paints_leads',
            },
        ),
    ]