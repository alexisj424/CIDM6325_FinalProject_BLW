# blogproject/urls.py
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),                 # login/logout
    path("blog/", include(("blog.urls", "blog"), namespace="blog")),        # existing blog
    path("blw/", include("blw.urls")),                                      # ✅ BLW app
    path("", RedirectView.as_view(pattern_name="blog:post_list", permanent=False)),
]

# Serve uploaded media in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)






