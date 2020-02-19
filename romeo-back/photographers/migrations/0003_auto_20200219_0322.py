# Generated by Django 3.0.3 on 2020-02-19 03:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('photographers', '0002_auto_20200217_0502'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photographer',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
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
        migrations.DeleteModel(
            name='PhotographerInfo',
        ),
    ]
