# Generated by Django 3.2.8 on 2021-11-15 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0009_participant_tip'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='answer',
            field=models.CharField(default=':', max_length=200),
        ),
        migrations.AddField(
            model_name='participant',
            name='hint',
            field=models.CharField(default=':', max_length=200),
        ),
    ]