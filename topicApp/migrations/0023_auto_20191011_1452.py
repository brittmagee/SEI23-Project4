# Generated by Django 2.1.11 on 2019-10-11 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topicApp', '0022_auto_20191011_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='isComplete',
            field=models.BooleanField(default=False),
        ),
    ]
