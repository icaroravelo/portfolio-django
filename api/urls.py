from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls import handler404, handler500
from django.conf.urls.static import static

from .views import (
    error404PageView,
    error500PageView,
    testPageView, 
    homePageView, 
    aboutPageView, 
    categoriesPageView, 
    schoolPageView, 
    contactPageView, 
    blogHomePageView,
    individualCategoryPageView,
    useTermsPageView,
    privacyPolicyPageView,
    cookiesPolicyPageView,
)

urlpatterns = [
    # Icaro Alves' Portfolio routes
    path('', homePageView, name='home'),
    path('sobre/', aboutPageView, name='sobre'),
    path('portfolio/', categoriesPageView, name='portfolio'), # Route for the entire portfolio
    path('categoria/<str:slug>/', individualCategoryPageView, name='categoria'), # Route for each category
    path('categoria/<str:slug>/projeto/<int:pk>/', individualCategoryPageView, name='projeto'), # Route for each project
    path('formacao/', schoolPageView, name='formacao'), # Route for education page
    path('certificados/', schoolPageView, name='certificados'), # Route for certificates (opening modal, so check it this route is really needed)
    path('contatos/', contactPageView, name='contatos'), # Route for contact page
    path('blog/', blogHomePageView, name='blog'), # Route for the entire blog
    path('post/<int:pk>/', blogHomePageView, name='post'), # Route for the post itself
    path('blog/categorias/<tags>/', blogHomePageView, name='post'), # Route for each tag of blog section

    # Error pages
    path('404/', error404PageView, name='error404Page'), 
    path('505/', error500PageView, name='error500Page'),

    # Legal pages
    path('termos-de-uso/', useTermsPageView, name='termos-de-uso'),
    path('politica-de-privacidade/', privacyPolicyPageView, name='politica-de-privacidade'),
    path('políticas-de-cookies/', cookiesPolicyPageView, name='politicas-de-cookies'),

    # Testing page
    path('teste/', testPageView, name='teste'),

    # Admin dashboard
    path('admin/', admin.site.urls),

    # Django Browser Reload
    path("__reload__/", include("django_browser_reload.urls")),
]

handler404 = 'api.views.error404PageView'

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)