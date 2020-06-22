# Generated by Django 3.0.3 on 2020-05-19 15:45

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('item', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='like',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]