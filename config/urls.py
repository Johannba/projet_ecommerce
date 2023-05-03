"""
Projet_ecommerce URL Configuration
"""

from django.contrib import admin
from django.urls import path, include
from django.views import defaults as default_views
from django.conf.urls.static import static
from django.conf import settings
import debug_toolbar

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("ecommerce.pages.urls")),
    path("users/", include("ecommerce.users.urls")),
    path('products/', include('ecommerce.products.urls', namespace='products')),
    path('__debug__/', include(debug_toolbar.urls)),  
]

if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    urlpatterns += (
        staticfiles_urlpatterns()
    )  # tell gunicorn where static files are in dev mode
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=str(settings.MEDIA_ROOT),
    )

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        

        urlpatterns = [
            path("__debug__/", include(debug_toolbar.urls))
        ] + urlpatterns
