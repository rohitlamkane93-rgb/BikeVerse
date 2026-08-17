from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User

from .models import Bike


# =====================================================
# HOME
# =====================================================

def home(request):

    if not request.user.is_authenticated:
        return redirect("register")

    bikes = Bike.objects.all().order_by("name")

    return render(
        request,
        "home.html",
        {
            "bikes": bikes
        }
    )


# =====================================================
# POPULAR BRANDS
# =====================================================

def popular_brands(request):

    if not request.user.is_authenticated:
        return redirect("login")

    brands = [
        "Hero",
        "Honda",
        "Yamaha",
        "KTM",
        "Royal Enfield",
        "TVS",
        "Bajaj",
    ]

    return render(
        request,
        "popular_brands.html",
        {
            "brands": brands
        }
    )


# =====================================================
# BRAND BIKES
# =====================================================

def brand_bikes(request, brand):

    if not request.user.is_authenticated:
        return redirect("login")

    bikes = Bike.objects.filter(
        brand__iexact=brand
    ).order_by("name")

    return render(
        request,
        "hero.html",
        {
            "bikes": bikes,
            "brand": brand
        }
    )


# =====================================================
# BIKE DETAIL
# =====================================================

def bike_detail(request, bike_id):

    if not request.user.is_authenticated:
        return redirect("login")

    bike = get_object_or_404(
        Bike,
        id=bike_id
    )

    return render(
        request,
        "bike_detail.html",
        {
            "bike": bike
        }
    )


# =====================================================
# SMART SEARCH
# =====================================================

def search_bikes(request):

    if not request.user.is_authenticated:
        return redirect("login")

    query = request.GET.get(
        "q",
        ""
    ).strip()

    bikes = Bike.objects.none()

    if query:

        bikes = Bike.objects.filter(
            Q(name__icontains=query) |
            Q(brand__icontains=query)
        ).order_by("name")

    return render(
        request,
        "search.html",
        {
            "bikes": bikes,
            "query": query
        }
    )


# =====================================================
# BIKE COMPARISON
# =====================================================

def compare_bikes(request):

    if not request.user.is_authenticated:
        return redirect("login")

    bike1_id = request.GET.get("bike1")
    bike2_id = request.GET.get("bike2")

    bike1 = None
    bike2 = None

    if bike1_id:

        try:
            bike1 = Bike.objects.get(
                id=bike1_id
            )
        except Bike.DoesNotExist:
            bike1 = None

    if bike2_id:

        try:
            bike2 = Bike.objects.get(
                id=bike2_id
            )
        except Bike.DoesNotExist:
            bike2 = None

    bikes = Bike.objects.all().order_by("name")

    return render(
        request,
        "compare.html",
        {
            "bikes": bikes,
            "bike1": bike1,
            "bike2": bike2
        }
    )


# =====================================================
# REGISTER
# =====================================================

def register_view(request):

    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":

        username = request.POST.get(
            "username",
            ""
        ).strip()

        email = request.POST.get(
            "email",
            ""
        ).strip()

        password = request.POST.get(
            "password",
            ""
        )

        confirm_password = request.POST.get(
            "confirm_password",
            ""
        )

        if not username or not email or not password:

            messages.error(
                request,
                "Please fill all required fields."
            )

            return render(
                request,
                "register.html"
            )

        if password != confirm_password:

            messages.error(
                request,
                "Passwords do not match."
            )

            return render(
                request,
                "register.html"
            )

        if User.objects.filter(
            username=username
        ).exists():

            messages.error(
                request,
                "Username already exists."
            )

            return render(
                request,
                "register.html"
            )

        if User.objects.filter(
            email=email
        ).exists():

            messages.error(
                request,
                "Email already registered."
            )

            return render(
                request,
                "register.html"
            )

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        user.save()

        messages.success(
            request,
            "Account created successfully! Please login."
        )

        return redirect("login")

    return render(
        request,
        "register.html"
    )


# =====================================================
# LOGIN
# =====================================================

def login_view(request):

    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":

        username = request.POST.get(
            "username",
            ""
        ).strip()

        password = request.POST.get(
            "password",
            ""
        )

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(
                request,
                user
            )

            return redirect("home")

        messages.error(
            request,
            "Invalid username or password."
        )

    return render(
        request,
        "login.html"
    )


# =====================================================
# LOGOUT
# =====================================================

def user_logout(request):

    logout(request)

    return redirect("register")