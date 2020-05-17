# Generated by Django 3.0.6 on 2020-05-13 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='farmhouse_detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('discription', models.CharField(max_length=1000)),
                ('mobile_no', models.IntegerField(default='')),
                ('email', models.EmailField(max_length=254)),
                ('cover_image', models.ImageField(upload_to='eventapp/images')),
            ],
        ),
    ]