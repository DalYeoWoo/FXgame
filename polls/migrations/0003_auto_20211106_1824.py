# Generated by Django 3.2.8 on 2021-11-06 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20211106_1606'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='participant',
            name='participant_id',
        ),
        migrations.AlterField(
            model_name='participant',
            name='Group',
            field=models.CharField(default='B', max_length=1),
        ),
        migrations.AlterField(
            model_name='participant',
            name='history',
            field=models.CharField(default=':', max_length=200),
        ),
    ]
