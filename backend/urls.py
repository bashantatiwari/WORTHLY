from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('predict/', include('vision.urls')),
    path('', include('accounts.urls')),
    path('', RedirectView.as_view(pattern_name='login', permanent=False)),
]
