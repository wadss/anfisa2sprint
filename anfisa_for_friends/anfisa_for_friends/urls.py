from django.contrib import admin
from django.urls import include, path
from django.conf import settings

if settings.DEBUG:
    import debug_toolbar

urlpatterns = [
    path('', include('homepage.urls')),
    path('about/', include('about.urls')),
    path('ice_cream/', include('ice_cream.urls')),
    path('admin/', admin.site.urls),
    path('__debug__/', include(debug_toolbar.urls)),
]
