from django.conf.urls import url
from . import views

urlpatterns = [
    url("^$", views.index, name="index"),
    url("^coin$", views.coin, name="coin"),
    url("^realtime$", views.realtime, name="realtime"),
]