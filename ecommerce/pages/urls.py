from django.urls import path, include

app_name = "pages"

urlpatterns = [
    path("", include("django.contrib.auth.urls")),
]