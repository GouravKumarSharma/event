# Generated by Django 3.0.6 on 2020-05-13 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventapp', '0003_user_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmhouse_detail',
            name='cover_image',
            field=models.ImageField(upload_to='eventapp/images'),
        ),
    ]
