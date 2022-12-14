# Generated by Django 4.1.1 on 2022-09-11 11:39

import datetime
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration', models.PositiveIntegerField()),
                ('name', models.CharField(choices=[('Trial', 'Trial'), ('Day', 'Day'), ('Month', 'Month'), ('Years', 'Years')], default='Trial', max_length=255)),
            ],
            options={
                'db_table': 'membership',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Reseller',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('credit', models.PositiveIntegerField()),
                ('create_admin', models.CharField(max_length=255)),
                ('isadmin', models.BooleanField(default=True)),
                ('username', models.CharField(max_length=255, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('Inactive', 'Inactive'), ('Active', 'Active')], default='Active', max_length=255)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Reseller',
                'verbose_name_plural': 'Resellers',
                'db_table': 'reseller',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('is_active', models.CharField(choices=[('ACTIVE', 'Active'), ('INACTIVE', 'Inactive')], default='ACTIVE', max_length=255)),
                ('start_date', models.DateTimeField(auto_now=True)),
                ('expire_date', models.DateField(default=datetime.date.today)),
                ('membership', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='membership', to='Customer.membership')),
                ('reseller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reseller', to='Customer.reseller')),
            ],
            options={
                'db_table': 'customer',
                'managed': True,
            },
        ),
    ]
