# Generated by Django 2.1.5 on 2019-05-03 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postapp', '0003_auto_20190503_0745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='writer',
            field=models.CharField(default='gyuzizi', max_length=20),
        ),
    ]