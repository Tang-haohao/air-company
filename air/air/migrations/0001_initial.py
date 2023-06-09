# Generated by Django 2.2.6 on 2023-05-05 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Air',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('airCode', models.CharField(max_length=100)),
                ('airCna', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('reserve1', models.CharField(max_length=100)),
                ('reserve2', models.CharField(max_length=100)),
                ('reserve3', models.CharField(max_length=100)),
                ('reserve4', models.CharField(max_length=100)),
                ('reserve5', models.CharField(max_length=100)),
                ('airC', models.CharField(max_length=100)),
                ('airF', models.CharField(max_length=100)),
                ('airFna', models.CharField(max_length=100)),
                ('airTotal', models.CharField(max_length=100)),
                ('airY', models.CharField(max_length=100)),
                ('airYna', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Air',
                'verbose_name_plural': 'Air',
                'db_table': 'air',
            },
        ),
    ]
