from django.forms import ModelForm
from .models import Listing


class ListingForm(ModelForm):
    class Meta:
        model = Listing
        fields = ['title', 'category', 'standard', 'address', 'city', 'area', 'zipcode', 'beds', 'baths', 'square_feet',
                  'description', 'price', 'photo_main', 'photo_1', 'photo_2', 'photo_3', 'photo_4', 'photo_5']


class UpdateForm(ModelForm):
    class Meta:
        model = Listing
        fields = ['title', 'area', 'description', 'price', 'photo_main', 'photo_1', 'photo_2', 'photo_3',
                  'photo_4', 'photo_5']
