# Generated by Django 4.2.5 on 2024-12-16 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usersession',
            old_name='start_time',
            new_name='created_at',
        ),
        migrations.AlterField(
            model_name='usersession',
            name='user',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]