from django.urls import path
from .views import *

app_name="coderpak"


urlpatterns = [
    path("", index, name="home"),
    path("detail",detail, name="details"),
]
