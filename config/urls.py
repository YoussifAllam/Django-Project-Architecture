from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse

third_party_urls = [
    path("ckeditor5/", include("django_ckeditor_5.urls")),
    path("site_administration/", admin.site.urls),
]

landing_page_urls = [
    # path("FAQ_and_terms/", include("apps.FAQ_and_terms.urls")),
]


urlpatterns = (
    [
        path("api/", include("apps.Users.urls")),
        path("registertion/", include("apps.registertion.urls")),
        path("health/", lambda request: HttpResponse("OK")),  # Health check endpoint
    ]
    + third_party_urls  # noqa
    + landing_page_urls  # noqa
)
if settings.DEBUG:
    import debug_toolbar

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += [path("__debug__/", include(debug_toolbar.urls))]
