# Generated by Django 3.0.1 on 2020-01-17 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('package_tracking', '0002_package_status_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='status_text',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
