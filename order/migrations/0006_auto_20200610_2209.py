# Generated by Django 3.0.3 on 2020-06-10 19:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_auto_20200531_2251'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['-creation_data']},
        ),
    ]
