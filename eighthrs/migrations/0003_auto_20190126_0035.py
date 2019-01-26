# Generated by Django 2.1.5 on 2019-01-26 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eighthrs', '0002_auto_20190126_0032'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100)),
                ('reps', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
