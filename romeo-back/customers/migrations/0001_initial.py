# Generated by Django 3.0.3 on 2020-04-01 18:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('photographers', '0002_photographer_style'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='users.CustomUserProfile')),
                ('fav_photographers', models.ManyToManyField(blank=True, null=True, related_name='fav_photographers', to='photographers.Photographer')),
            ],
        ),
    ]
