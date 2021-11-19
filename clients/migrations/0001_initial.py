# Generated by Django 3.2.9 on 2021-11-19 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(error_messages={'unique': 'This email is been using for other user'}, max_length=254, unique=True, verbose_name='email address')),
                ('first_name', models.CharField(blank=True, max_length=70, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=80, verbose_name='last name')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
