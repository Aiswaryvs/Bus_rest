# Generated by Django 4.1.1 on 2022-10-10 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bus', '0004_alter_price_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='buslist',
            name='price',
            field=models.PositiveIntegerField(default=100),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Price',
        ),
    ]
