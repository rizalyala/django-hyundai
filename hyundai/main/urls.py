from django.urls import path
from . import views

urlpatterns = [
    # ex: //
    path("", views.home, name="home"),
    path("/<int:id>/", views.vehicle_detail, name="vehicle_detail"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
]