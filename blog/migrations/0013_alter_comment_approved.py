# Generated by Django 4.2.17 on 2025-02-23 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_alter_comment_approved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='approved',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
