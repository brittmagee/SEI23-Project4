# Generated by Django 2.1.11 on 2019-10-11 21:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('topicApp', '0025_auto_20191011_2052'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='bike',
        ),
    ]
