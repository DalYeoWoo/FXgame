# Generated by Django 3.2.8 on 2021-11-06 09:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20211106_1824'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='participant',
            name='Group',
        ),
    ]
