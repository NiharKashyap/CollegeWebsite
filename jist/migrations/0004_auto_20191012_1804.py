# Generated by Django 2.2 on 2019-10-12 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jist', '0003_studetails'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='name',
            field=models.CharField(default='nam', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='studetails',
            name='image',
            field=models.ImageField(upload_to='media/'),
        ),
    ]