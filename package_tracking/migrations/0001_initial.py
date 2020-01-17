# Generated by Django 3.0.1 on 2020-01-17 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tracking_number', models.CharField(max_length=100, unique=True)),
                ('service_name', models.CharField(choices=[('UPS', 'UPS'), ('USPS', 'USPS')], max_length=5)),
            ],
        ),
    ]
