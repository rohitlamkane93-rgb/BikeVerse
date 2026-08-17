from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from bikeverse import views


urlpatterns = [

    # ================= HOME =================

    path(
        "",
        views.home,
        name="home"
    ),


    # ================= ADMIN =================

    path(
        "admin/",
        admin.site.urls
    ),


    # ================= POPULAR BRANDS =================

    path(
        "brands/",
        views.popular_brands,
        name="popular_brands"
    ),


    # ================= BRAND BIKES =================

    path(
        "brand/<str:brand>/",
        views.brand_bikes,
        name="brand_bikes"
    ),


    # ================= BIKE DETAIL =================

    path(
        "bike/<int:bike_id>/",
        views.bike_detail,
        name="bike_detail"
    ),


    # ================= SEARCH =================

    path(
        "search/",
        views.search_bikes,
        name="search_bikes"
    ),


    # ================= COMPARE =================

    path(
        "compare/",
        views.compare_bikes,
        name="compare_bikes"
    ),


    # ================= REGISTER =================

    path(
        "register/",
        views.register_view,
        name="register"
    ),


    # ================= LOGIN =================

    path(
        "login/",
        views.login_view,
        name="login"
    ),


    # ================= LOGOUT =================

    path(
        "logout/",
        views.user_logout,
        name="logout"
    ),

]


# ================= MEDIA FILES =================

if settings.DEBUG:

    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )