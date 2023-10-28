from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.views.generic RedirectView
from django.conf import settings
from django.conf.urls.static import static

# https://localhost:8000/
urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include("blog.urls"),
    path('admin/', RedirectView.as_view(url="/blog/", permanent = True)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
