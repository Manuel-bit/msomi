# Generated by Django 3.1.1 on 2020-09-06 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='media/profile_pics'),
        ),
        migrations.AddField(
            model_name='tutor',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='media/profile_pics'),
        ),
    ]