# Generated by Django 3.0.6 on 2020-05-23 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dreamtours_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='particular',
            name='address',
            field=models.CharField(default='', max_length=150),
        ),
    ]
