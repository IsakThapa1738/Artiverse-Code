# Generated by Django 5.0.6 on 2024-06-25 19:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Artists', '0003_alter_artist_user'),
        ('Artworks', '0009_alter_artwork_artist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artwork',
            name='artist',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='arts', to='Artists.artist'),
        ),
    ]
