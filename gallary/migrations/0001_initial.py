# Generated by Django 3.2.8 on 2021-10-12 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('create_by', models.CharField(max_length=35)),
                ('img', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
