from django.contrib import admin
from django.urls import path, include

from .views import testPageView, homePageView

urlpatterns = [
    path('', homePageView, name='home'),
    path('teste/', testPageView),

    path('admin/', admin.site.urls),
    path('', include('example.urls')),

    path("__reload__/", include("django_browser_reload.urls")),
]

