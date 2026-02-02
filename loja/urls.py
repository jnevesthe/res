
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns=[

    path('', views.home, name='home'),
    #path('pratos/', views.pratos, name='pratos'),
    path('promo/', views.pratos, name='promo'),
    path('contatos/', views.contatos, name='contatos'),
    
    path('categorias/', views.pratos_categoria, name='categoria'),  # lista todas categorias
    path('pratos/<int:categoria_id>/', views.pratos, name='pratos'),  # pratos de uma categoria





]


# Serve arquivos estáticos e mídia no DEBUG (Termux)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
    