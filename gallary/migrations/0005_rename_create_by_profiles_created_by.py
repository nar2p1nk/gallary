# Generated by Django 3.2.8 on 2021-10-13 20:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallary', '0004_rename_content_profiles'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profiles',
            old_name='create_by',
            new_name='created_by',
        ),
    ]
