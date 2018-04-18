from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User


REGION_CHOICES = (
    ('North', 'North'),
    ('East', 'East'),
    ('South', 'South'),
    ('West', 'West'),
    ('Central', 'Central'),
)

WEATHER_CHOICES = (
    ('Clear', 'Clear'),
    ('Rain', 'Rain'),
    ('Snow', 'Snow'),
    ('Cloudy', 'Cloudy')
)


# Create your models here.
class Ticket(models.Model):
    id = models.AutoField(primary_key=True)
    location = models.CharField(max_length=30)
    date_received = models.DateField()
    time_marked = models.TimeField()
    time_issued = models.TimeField()
    time_limit = models.IntegerField()
    region = models.CharField(max_length=8, choices=REGION_CHOICES)
    weather = models.CharField(max_length=6, choices=WEATHER_CHOICES)
    username = models.ForeignKey(User, on_delete=models.CASCADE)


class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ['location', 'date_received', 'time_marked', 'time_issued', 'time_limit', 'region', 'weather']


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']