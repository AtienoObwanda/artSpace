# Generated by Django 4.0.4 on 2022-05-28 16:39

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('space', '0003_alter_image_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], force_format=None, keep_meta=True, quality=75, size=[2878, 1618], upload_to='art/'),
        ),
    ]
