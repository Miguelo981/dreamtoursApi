# Generated by Django 3.0.6 on 2020-05-25 20:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dreamtours_app', '0007_auto_20200525_2059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='particular',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dreamtours_app.Particular'),
        ),
    ]