# Generated by Django 3.2.5 on 2021-08-23 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_website', models.CharField(default='rrrrat.com', max_length=64, verbose_name='主网站')),
                ('title', models.CharField(default="rrrrat'blog", max_length=20, verbose_name='标题')),
                ('website_number', models.CharField(default='京ICP备2020034849号-1', max_length=100, verbose_name='备案号')),
                ('website_logo', models.ImageField(default='', upload_to='logo', verbose_name='网站logo')),
            ],
        ),
    ]
