# Generated by Django 4.1.1 on 2022-09-08 11:43

import datetime
from django.db import migrations, models
import django.db.models.deletion


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
                ('name', models.CharField(choices=[('Trial', 'Trial'), ('Day', 'Day'), ('Month', 'Month'), ('Years', 'Years')], default='DY', max_length=255)),
            ],
            options={
                'db_table': 'membership',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Reseller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('RESELLER', 'Reseller'), ('ADMIN', 'admin')], default='ADMIN', max_length=255)),
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
        migrations.CreateModel(
            name='Credit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('credit', models.PositiveIntegerField()),
                ('add', models.DateTimeField(auto_now=True)),
                ('reseller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='credit_reseller', to='Customer.reseller')),
            ],
            options={
                'verbose_name': 'Credit',
                'verbose_name_plural': 'Credits',
                'db_table': 'Credit',
                'managed': True,
            },
        ),
    ]