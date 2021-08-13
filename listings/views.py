from django.shortcuts import render, get_object_or_404, redirect, HttpResponse, HttpResponseRedirect, reverse, loader
from .models import Listing
from django.core.paginator import Paginator
from .choices import category_choices, area_choices, standard_choices
from listings.forms import ListingForm, UpdateForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib import messages


def listings(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    page_listing = paginator.get_page(page)
    context = {
        'listings': page_listing
    }

    return render(request, 'listings/listings.html', context)


def listing(request, pk):
    rate = False
    favourite = False
    listing = get_object_or_404(Listing, pk=pk)

    if request.user.is_authenticated:
        favourites = str(request.user.favourites)
        rate_listing = str(request.user.rate_listing)
        favourites = favourites.split(',')
        rate_listing = rate_listing.split(',')
        if request.method == "POST":
            if 'favourite_val' in request.POST:
                favourite_val = request.POST['favourite_val']
                if favourite_val == 'unfavourite':
                    if str(pk) in favourites:
                        favourites.remove(str(pk))
                if favourite_val == 'favourite':
                    if str(pk) not in favourites:
                        favourites.append(str(pk))
                request.user.favourites = ','.join(favourites)
                request.user.save()

            if 'my_rating' in request.POST:
                my_rating = request.POST['my_rating']
                if int(my_rating) > 5 or int(my_rating) < 1:
                    messages.error(request, 'Please enter a value from 1-5')
                elif str(pk) not in rate_listing:
                    if listing.total_rating:
                        listing.total_rating += int(request.POST['my_rating'])
                        listing.no_of_rating += 1
                    else:
                        listing.total_rating = int(request.POST['my_rating'])
                        listing.no_of_rating = 1
                    rate_listing.append(str(pk))
                    request.user.rate_listing = ','.join(rate_listing)
                    request.user.save()
                    listing.save()

        if str(pk) in favourites:
            favourite = True
        if str(pk) not in rate_listing:
            rate = True
    current_rating = 0
    if listing.no_of_rating:
        current_rating = listing.total_rating / listing.no_of_rating
    context = {
        'listing': listing,
        'favourite': favourite,
        'rate': rate,
        'current_rating': current_rating

    }
    return render(request, 'listings/listing.html', context)


def search(request):
    query_set = Listing.objects.order_by('list_date').reverse()
    if 'text' in request.GET:
        keywords = request.GET['text']
        if keywords:
            query_set = query_set.filter(Q(title__icontains=keywords) | Q(description__icontains=keywords))
    if 'category' in request.GET:
        category = request.GET['category']
        if category:
            query_set = query_set.filter(category__iexact=category)
    if 'standard' in request.GET:
        standard = request.GET['standard']
        if standard:
            query_set = query_set.filter(standard__iexact=standard)
    if 'area' in request.GET:
        area = request.GET['area']
        if area:
            query_set = query_set.filter(area__iexact=area)
    context = {
        'query_set': query_set,
        'keywords': keywords,
        'area_choices': area_choices,
        'standard_choices': standard_choices,
        'category_choices': category_choices,
        'values': request.GET
    }
    return render(request, 'listings/search.html', context)


@login_required
def create(request):
    if request.method == 'POST':
        form = ListingForm(request.POST, request.FILES)
        if form.is_valid():
            new = form.save(commit=False)
            new.owner = request.user
            new.save()
            return redirect('dashboard')
        else:
            return render(request, 'listings/create.html', {'form': form})

    else:
        return render(request, 'listings/create.html', {'form': ListingForm()})


@login_required
def update(request, pk):
    listing = get_object_or_404(Listing, pk=pk, owner=request.user)
    context = {
        'form': UpdateForm(instance=listing),
        'update': True,
        'pk': pk
    }
    if request.method == "POST":
        form = UpdateForm(request.POST, request.FILES, instance=listing)
        print(form)
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    else:
        return render(request, 'listings/update.html', context)

@login_required
def delete_listing(request, pk):
    if request.user.is_superuser:
        listing = get_object_or_404(Listing, pk=pk)
        listing.delete()
        return redirect('admin')
    else:
        listing = get_object_or_404(Listing, pk=pk, owner=request.user)
    if request.method == "POST":
        listing.delete()
        return redirect('dashboard')