# Generated by Django 2.2.6 on 2019-10-28 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jist', '0005_auto_20191027_1903'),
    ]

    operations = [
        migrations.AddField(
            model_name='studetails',
            name='gender',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='studetails',
            name='phone_no',
            field=models.CharField(max_length=12),
        ),
    ]