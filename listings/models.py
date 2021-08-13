from django.db import models
from datetime import datetime
from core.models import User


class Listing(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100, choices={('Boys', 'Boys'), ('Girls', 'Girls'), ('Both', 'Both')})
    standard = models.CharField(max_length=100, choices={('Silver', 'Silver'), ('Gold', 'Gold'), ('Diamond', 'Diamond')})
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100, choices={('Lahore', 'Lahore')})
    area = models.CharField(max_length=100, choices={ ('DHA', 'DHA'), ('Gulberg', 'Gulberg'),
                                                     ('Johar Town', 'Johar Town'), ('Township', 'Township'),('Iqbal Town', 'Iqbal Town'),
                                                     ('Model Town', 'Model Town'), ('Wapda Town', 'Wapda Town'), ('Central Park', 'Central Park'),
                                                     ('Valencia Town', 'Valencia Town'), ('Behria Town', 'Behria Town'), ('Askari', 'Askari'),
                                                     ('Sadar', 'Sadar'), ('Ferozpur Road', 'Ferozpur Road',),( 'Jalo', 'Jalo'),
                                                     ('Thokar', 'Thokar'),('Ichra', 'Ichra'), ('Canal Road', 'Canal Road'), ('Mall Road', 'Mall Road'),
                                                     ('Lakshmi Chock', 'Lakshmi Chock')})
    zipcode = models.CharField(max_length=10)
    beds = models.PositiveIntegerField(null=True)
    baths = models.PositiveIntegerField(null=True)
    square_feet = models.DecimalField(max_digits=64, decimal_places=2, null=True)
    description = models.TextField(blank=False)
    price = models.IntegerField()
    total_rating = models.IntegerField(null=True, blank=True)
    no_of_rating = models.IntegerField(null=True, blank=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateField(default=datetime.now)
    rent_agreement = models.FileField(default='/Tenancy_Agreement.pdf', blank=True)

    def __str__(self):
        return self.title
