# Generated by Django 3.0.3 on 2020-03-25 19:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('photographers', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Style',
            fields=[
                ('style_name', models.CharField(choices=[('GRADUATION', 'Graduation'), ('LANDSCAPE', 'Landscape'), ('PORTRAIT', 'Portrait'), ('PRODUCT', 'Product'), ('FASHION', 'Fashion'), ('EVENT', 'Event'), ('WEDDING', 'Wedding'), ('NONE', 'None')], max_length=20, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Photographer',
            fields=[
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='users.CustomUserProfile')),
                ('photographer_last_online_time', models.DateTimeField(blank=True, null=True)),
                ('photographer_avail_time', models.ManyToManyField(blank=True, null=True, to='photographers.AvailTime')),
                ('photographer_equipment', models.ManyToManyField(blank=True, null=True, related_name='photographer_equipment', to='photographers.Equipment')),
                ('photographer_photos', models.ManyToManyField(blank=True, null=True, related_name='photographer_photos', to='photographers.Photo')),
                ('photographer_style', models.ManyToManyField(blank=True, null=True, related_name='styles', to='photographers.Style')),
            ],
        ),
    ]
