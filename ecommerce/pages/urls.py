from django.urls import path, include

from ecommerce.pages.views import home_view


app_name = "pages"

urlpatterns = [
    path("home/", home_view, name= "home"),
]