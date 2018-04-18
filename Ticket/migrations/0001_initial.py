# Generated by Django 2.0.4 on 2018-04-18 18:00

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
            name='Ticket',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('location', models.CharField(max_length=30)),
                ('date_received', models.DateField()),
                ('time_marked', models.TimeField()),
                ('time_issued', models.TimeField()),
                ('time_limit', models.IntegerField()),
                ('region', models.CharField(choices=[('North', 'North'), ('East', 'East'), ('South', 'South'), ('West', 'West'), ('Central', 'Central')], max_length=8)),
                ('weather', models.CharField(choices=[('Clear', 'Clear'), ('Rain', 'Rain'), ('Snow', 'Snow'), ('Cloudy', 'Cloudy')], max_length=6)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
