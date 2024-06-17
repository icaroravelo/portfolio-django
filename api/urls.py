from django.contrib import admin
from django.urls import path, include

from .views import testPageView, homePageView, aboutPageView, categoriesPageView, schoolPageView, contactPageView, blogHomePageView

urlpatterns = [
    path('', homePageView, name='home'),
    path('sobre/', aboutPageView, name='sobre'),
    path('portfolio/', categoriesPageView, name='portfolio'),
    path('educacao/', schoolPageView, name='educacao'),
    path('contato/', contactPageView, name='contato'),
    path('blog/', blogHomePageView, name='blog'),

    path('teste/', testPageView, name='teste'),

    path('admin/', admin.site.urls),
    path('', include('example.urls')),

    path("__reload__/", include("django_browser_reload.urls")),
]

