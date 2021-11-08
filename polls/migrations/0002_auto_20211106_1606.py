# Generated by Django 3.2.8 on 2021-11-06 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Flow_Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exchange_rate', models.FloatField(default=0.0)),
                ('time_second', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='participant',
            name='Group',
            field=models.CharField(default='A', max_length=1),
        ),
        migrations.AlterField(
            model_name='participant',
            name='participant_id',
            field=models.CharField(default='61641', max_length=6),
        ),
    ]