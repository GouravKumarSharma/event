# Generated by Django 3.0.6 on 2020-05-13 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventapp', '0002_auto_20200513_2215'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_name', models.CharField(max_length=100)),
                ('email', models.EmailField(default='', max_length=254)),
                ('u_number', models.IntegerField(default='')),
                ('u_image', models.ImageField(upload_to='eventapp/images')),
            ],
        ),
    ]
