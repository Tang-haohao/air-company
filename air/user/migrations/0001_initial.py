# Generated by Django 3.2.18 on 2023-03-27 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=20, verbose_name='姓名')),
                ('password', models.CharField(blank=True, max_length=20, verbose_name='密码')),
                ('type', models.IntegerField()),
            ],
            options={
                'verbose_name': '用户模块',
                'verbose_name_plural': '用户模块',
                'db_table': 'user_info',
            },
        ),
    ]
