# Generated by Django 3.0.3 on 2020-02-12 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ReviewInfo',
            fields=[
                ('ReviewID', models.AutoField(primary_key=True, serialize=False)),
                ('ReviewDetail', models.TextField()),
            ],
        ),
    ]
