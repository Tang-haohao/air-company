# Generated by Django 2.2.6 on 2023-05-05 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('role', models.IntegerField()),
                ('status', models.CharField(max_length=100)),
                ('reserve1', models.CharField(max_length=100)),
                ('reserve2', models.CharField(max_length=100)),
                ('reserve3', models.CharField(max_length=100)),
                ('reserve4', models.CharField(max_length=100)),
                ('reserve5', models.CharField(max_length=100)),
                ('create_time', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'User',
                'db_table': 'user',
            },
        ),
        migrations.DeleteModel(
            name='UserInfo',
        ),
    ]
