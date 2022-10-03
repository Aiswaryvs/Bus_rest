# Generated by Django 4.1.1 on 2022-10-03 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bus', '0004_user_alter_reservation_user'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='user',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
    ]
