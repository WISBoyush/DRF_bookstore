# Generated by Django 4.1.1 on 2022-09-16 11:28

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(choices=[('CART', 'In cart'), ('AWAITING_ARRIVAL', 'Awaiting_arrival'), ('AWAITING_PAYMENT', 'Awaiting payment'), ('PAID', 'Paid'), ('AWAITING_DELIVERY', 'Awaiting delivery'), ('SENT', 'Sent'), ('FINISHED', 'Finished')], default='CART', max_length=50, verbose_name='State')),
                ('orders_id', models.CharField(blank=True, max_length=250, null=True, verbose_name="Order's id")),
                ('rented_from', models.DateField(default=datetime.date.today, verbose_name='Rented from')),
                ('rented_to', models.DateField(default=datetime.date.today, verbose_name='Rented to')),
                ('city', models.CharField(default='12345', max_length=100, verbose_name='City to delivery')),
                ('address', models.CharField(default='12345', max_length=100, verbose_name='Address to delivery')),
                ('item', models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='main.item', verbose_name='Item')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]