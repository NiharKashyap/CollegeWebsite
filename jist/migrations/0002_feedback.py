# Generated by Django 2.2.5 on 2019-09-19 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jist', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cmnt', models.CharField(max_length=1024)),
                ('rating', models.FloatField()),
            ],
        ),
    ]