from django.urls import path

from . import views

app_name="encyclopedia"

urlpatterns = [
    path("", views.index, name="index"),
    path("random/", views.rand, name="rand"),
    path("new/", views.new, name="new"),
    path("results/", views.results, name="results"),
    path("wiki/<str:title>", views.search, name="search"),
    path("wiki/<str:title>/edit", views.edit, name="edit"),

]
