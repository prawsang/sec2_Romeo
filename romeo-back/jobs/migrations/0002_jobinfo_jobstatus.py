# Generated by Django 3.0.3 on 2020-02-12 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobinfo',
            name='JobStatus',
            field=models.CharField(choices=[('TEST', 'Test')], default=1, max_length=4),
            preserve_default=False,
        ),
    ]
