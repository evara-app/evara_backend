import os
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("api/v1/", include(("apps.api.urls", "api"))),
]

if os.environ.get("DJANGO_SETTINGS_MODULE") == "config.settings.production":
    urlpatterns += [
        path("dfjeuhhdhsgdthahdhdhfkdklleewooiaujsjsau/", admin.site.urls),
        path("api/v1/", include(("apps.api.urls", "api"))),
    ]
else:
    from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

    urlpatterns += [
        path("admin/", admin.site.urls),
        path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
        path(
            "api/swagger/",
            SpectacularSwaggerView.as_view(url_name="schema"),
            name="swagger-ui",
        ),
    ]
