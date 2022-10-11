# Generated by Django 4.0.7 on 2022-10-10 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_title', models.CharField(max_length=50, verbose_name="Tag's title")),
                ('tag_description', models.CharField(max_length=100, verbose_name="Tag's description")),
                ('discount', models.IntegerField(default=0, verbose_name='Discount')),
            ],
        ),
    ]