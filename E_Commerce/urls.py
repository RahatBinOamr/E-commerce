
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import (
 handler404
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('product.urls')),
    path('',include('dashboard.urls')),
    path('',include('UserProfile.urls')),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
handler404 = 'product.views.not_found'