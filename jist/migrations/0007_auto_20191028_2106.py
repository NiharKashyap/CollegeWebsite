# Generated by Django 2.2.6 on 2019-10-28 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jist', '0006_auto_20191028_0746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='rating',
            field=models.CharField(max_length=255),
        ),
    ]
