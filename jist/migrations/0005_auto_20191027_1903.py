# Generated by Django 2.2.6 on 2019-10-27 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jist', '0004_auto_20191012_1804'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studetails',
            old_name='name',
            new_name='fname',
        ),
        migrations.AddField(
            model_name='studetails',
            name='addr',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studetails',
            name='email',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studetails',
            name='lname',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studetails',
            name='phone_no',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='studetails',
            name='semester',
            field=models.IntegerField(),
        ),
    ]