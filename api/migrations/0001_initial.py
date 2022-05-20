# Generated by Django 4.0.4 on 2022-05-18 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coronavirus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=50)),
                ('total_cases', models.CharField(max_length=50)),
                ('new_cases', models.CharField(max_length=50)),
                ('total_deaths', models.CharField(max_length=50)),
                ('new_deaths', models.CharField(max_length=50)),
                ('total_recovered', models.CharField(max_length=50)),
                ('active_cases', models.CharField(max_length=50)),
                ('total_tests', models.CharField(max_length=50)),
                ('population', models.CharField(max_length=50)),
                ('continent', models.CharField(max_length=50)),
                ('slug', models.SlugField(blank=True)),
            ],
            options={
                'verbose_name': 'coronavirus',
                'verbose_name_plural': 'coronavirus',
            },
        ),
    ]
