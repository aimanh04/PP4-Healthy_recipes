# Generated by Django 4.2.17 on 2025-02-21 23:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_about_feat_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='about',
            old_name='feat_image',
            new_name='featured_image',
        ),
    ]
