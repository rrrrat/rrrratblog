# Generated by Django 3.2.5 on 2021-08-23 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, default='/static/images/users/avatar-001.jpg', upload_to='users_avatar', verbose_name='用户头像'),
        ),
    ]
