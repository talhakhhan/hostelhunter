from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
                  path('admin/', admin.site.urls),
                  url(r'/', include('hostel.urls')),
                  url(r'^$', views.home, name="home"),
                  path('listings/', include('listings.urls')),
                  path('accounts/', include('accounts.urls')),
                  path('contact/', include('inquiry.urls')),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
