from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# from hostel.decorators import unauthenticated_user, allowed_users
from listings.choices import category_choices, area_choices
from listings.models import Listing


def home(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:6]
    context = {
        'listings': listings,
        'area_choices': area_choices,
        'category_choices': category_choices,
    }

    return render(request, "home.html", context)
