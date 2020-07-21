from django.urls import path

from . import views

app_name="wiki"
urlpatterns = [
    path("", views.index, name="index"),
    path("search/", views.search, name="search"),
    path("edit/", views.edit, name="edit"),
    path("randompage/", views.randompage, name="randompage"),
    path("create", views.create, name="create")
]
