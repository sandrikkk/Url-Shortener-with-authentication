# Generated by Django 4.0.6 on 2023-01-08 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('url_shortener_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]
