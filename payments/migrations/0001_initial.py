# Generated by Django 2.2.3 on 2019-11-06 10:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        ('properties', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LNMOnline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checkout_request_id', models.CharField(max_length=99)),
                ('merchant_request_id', models.CharField(max_length=99)),
                ('result_code', models.IntegerField()),
                ('result_desc', models.CharField(max_length=120)),
                ('amount', models.FloatField(null=True)),
                ('mpesa_receipt_number', models.CharField(max_length=18, null=True)),
                ('phone_number', models.CharField(max_length=13, null=True)),
                ('timestamp', models.DateTimeField(null=True)),
            ],
            options={
                'verbose_name': 'Transaction',
                'verbose_name_plural': 'Transactions',
                'ordering': ('timestamp',),
            },
        ),
        migrations.CreateModel(
            name='PaymentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField()),
                ('amount', models.FloatField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('merchant_request_id', models.CharField(max_length=99, null=True)),
                ('checkout_request_id', models.CharField(max_length=99, null=True)),
                ('valid_until', models.DateTimeField(null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(default='Pending', max_length=10)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.Profile')),
                ('payment_type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='payments.PaymentType')),
                ('property_item', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='properties.Property')),
                ('transaction', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='payments.LNMOnline')),
            ],
            options={
                'ordering': ['-timestamp'],
                'get_latest_by': 'timestamp',
            },
        ),
    ]
