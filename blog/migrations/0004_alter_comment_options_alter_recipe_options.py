# Generated by Django 4.2.17 on 2024-12-31 00:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['created_on']},
        ),
        migrations.AlterModelOptions(
            name='recipe',
            options={'ordering': ['-created_on', 'author']},
        ),
    ]