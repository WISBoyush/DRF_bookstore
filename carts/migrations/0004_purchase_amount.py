# Generated by Django 4.0.7 on 2022-09-26 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0003_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='amount',
            field=models.IntegerField(default=1, verbose_name='Amount of items'),
        ),
    ]