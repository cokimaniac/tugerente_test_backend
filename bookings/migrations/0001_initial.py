# Generated by Django 3.2.9 on 2021-11-19 13:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_ammount', models.FloatField(default=0.0)),
                ('total_to_pay', models.FloatField(default=0.0)),
                ('state', models.CharField(choices=[('PEND', 'Pending'), ('PAID', 'Paid'), ('REMO', 'Removed')], default='PEND', max_length=15)),
                ('stay_days', models.IntegerField(default=None)),
                ('reserved_at', models.DateTimeField(auto_now=True)),
                ('reserved_for', models.DateTimeField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
