# Generated by Django 3.0.3 on 2020-02-13 11:04

from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AvailTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AvailDate', models.DateTimeField()),
                ('AvailTime', models.CharField(choices=[('HALF_DAY_MORNING', 'Half-day(Morning-Noon)'), ('HALF_DAY_NOON', 'Half-day(Noon-Evening)'), ('FULL_DAY', 'Full-Day'), ('NIGHT', 'Night'), ('FULL_DAY_NIGHT', 'Full-Day and Night')], max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('EquipmentID', models.AutoField(primary_key=True, serialize=False)),
                ('EquipmentName', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('PhotoID', models.AutoField(primary_key=True, serialize=False)),
                ('PhotoLink', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='PhotographerInfo',
            fields=[
                ('PhotographerID', models.AutoField(primary_key=True, serialize=False)),
                ('PhotographerFName', models.CharField(max_length=50)),
                ('PhotographerLName', models.CharField(max_length=50)),
                ('PhotographerSSN', models.CharField(max_length=13)),
                ('PhotographerEmail', models.EmailField(max_length=254)),
                ('PhotographerPassword', models.CharField(max_length=50)),
                ('PhotographerContact', models.CharField(max_length=100)),
                ('PhotographerPrice', models.FloatField()),
                ('PhotographerLastOnlineTime', models.DateTimeField()),
                ('PhotographerPaymentInfo', models.TextField()),
                ('PhotographerStyle', multiselectfield.db.fields.MultiSelectField(choices=[('GRADUATION', 'Graduation'), ('LANDSCAPE', 'Landscape'), ('PORTRAIT', 'Portrait'), ('PRODUCT', 'Product'), ('FASHION', 'Fashion'), ('EVENT', 'Event'), ('WEDDING', 'Wedding')], max_length=59)),
                ('PhotographerAvailTime', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photographer_avail_time', to='photographers.AvailTime')),
                ('PhotographerEquipment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photographer_equipment', to='photographers.Equipment')),
                ('PhotographerPhotos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photographer_photos', to='photographers.Photo')),
            ],
        ),
    ]