# Generated by Django 4.0.3 on 2022-03-25 08:43

from django.db import migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=sorl.thumbnail.fields.ImageField(upload_to='profiles'),
        ),
    ]
