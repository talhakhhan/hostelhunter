from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


# @admin_only
def hostels(request):
    return render(request, "Hostels.html", )


def contact(request):
    return render(request, "contact.html")


def about(request):
    return render(request, "about.html")


def boys_hostel(request):
    return render(request, "boys_hostel.html")


def signup(request):
    return render(request, "signup.html")


# def loginUser(request):
#
#     return render(request, "login.html")
#
#
#
# def logoutUser(request):
#     # logout(request)
#     return redirect ('hostel:login')


def girls_hostel(request):
    return render(request, "girls_hostel.html")


def userPage(request):
    context = {}
    return render(request, "user.html", context)
