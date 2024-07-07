from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import (
    errorPageView,
    testPageView, 
    homePageView, 
    aboutPageView, 
    categoriesPageView, 
    schoolPageView, 
    contactPageView, 
    blogHomePageView,
    individualCategoryPageView
)

urlpatterns = [
    path('', homePageView, name='home'),
    path('sobre/', aboutPageView, name='sobre'),
    path('portfolio/', categoriesPageView, name='portfolio'), # Route for the entire portfolio
    path('categoria/<str:slug>/', individualCategoryPageView, name='categoria'), # Route for each category
    path('educacao/', schoolPageView, name='educacao'), 
    path('contato/', contactPageView, name='contato'),
    path('blog/', blogHomePageView, name='blog'), # Route for the entire blog
    path('post/<int:pk>/', blogHomePageView, name='post'), # Route for the post itself
    path('blog/categorias/<tags>/', blogHomePageView, name='post'), # Route for each tag of blog section

    path('pagina-de-erro/', errorPageView, name='errorPage'),

    path('teste/', testPageView, name='teste'),

    path('admin/', admin.site.urls),

    path("__reload__/", include("django_browser_reload.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)