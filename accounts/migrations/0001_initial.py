# Generated by Django 3.2.5 on 2021-08-23 03:39

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('moblie', models.CharField(max_length=255, null=True, verbose_name='电话号码')),
                ('avatar', models.ImageField(blank=True, default='static/images/icon/user.gif', upload_to='users_avatar', verbose_name='用户头像')),
                ('status', models.CharField(default=1, max_length=255, null=True, verbose_name='状态')),
                ('wechart', models.CharField(blank=True, default=1, max_length=50, null=True, verbose_name='微信')),
                ('qq', models.CharField(blank=True, default=1, max_length=10, null=True, verbose_name='QQ')),
                ('blog_address', models.CharField(blank=True, default='localhost', max_length=100, null=True, verbose_name='博客地址')),
                ('introduction', models.TextField(blank=True, default='爸爸的爸爸是爷爷', max_length=500, verbose_name='自我介绍')),
                ('value1', models.CharField(default=1, max_length=255, null=True, verbose_name='value1')),
                ('value2', models.CharField(default=1, max_length=255, null=True, verbose_name='value2')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': '用户信息',
                'verbose_name_plural': '用户信息',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
