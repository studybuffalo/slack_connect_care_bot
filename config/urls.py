"""Base URLs for Slack Connect Care Bot."""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    # Django Admin URLs
    path(settings.ADMIN_URL, admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    from django.views import defaults as default_views

    import debug_toolbar

    urlpatterns += [
        # Error pages for debugging
        path('400/', default_views.bad_request, kwargs={'exception': Exception('Bad Request!')}),
        path('403/', default_views.permission_denied, kwargs={'exception': Exception('Permission Denied')}),
        path('404/', default_views.page_not_found, kwargs={'exception': Exception('Page not Found')}),
        path('500/', default_views.server_error),

        # Debug toolbar
        path('__debug__/', include(debug_toolbar.urls)),
    ]
