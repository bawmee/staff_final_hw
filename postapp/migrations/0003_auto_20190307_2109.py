# Generated by Django 2.1.5 on 2019-03-07 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postapp', '0002_post_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='genre',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='post',
            name='review',
            field=models.TextField(max_length=150),
        ),
        migrations.AlterField(
            model_name='post',
            name='site',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='post',
            name='writer',
            field=models.CharField(max_length=15),
        ),
    ]
