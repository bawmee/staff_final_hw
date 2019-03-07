# Generated by Django 2.1.5 on 2019-02-26 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site', models.CharField(max_length=20)),
                ('contry', models.CharField(max_length=15)),
                ('genre', models.CharField(max_length=20)),
                ('rate', models.IntegerField()),
                ('review', models.TextField(max_length=250)),
                ('date', models.DateTimeField(verbose_name='date published')),
                ('writer', models.CharField(max_length=20)),
            ],
        ),
    ]
