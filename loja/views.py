from django.shortcuts import render
from .models import (
    SiteInfo,
    Slogan,
    HomeBanner,
    HomeCategoria,
    PratoDestaque,
    CategoriaPrato,
    HomeBloco,
    Promocao,
    Contato,
    Horario
)

# =======================
# CONTEXTO BASE (GLOBAL)
# =======================

"""
def base_context():
    return {
        'site_info': SiteInfo.objects.first(),
        'slogan': Slogan.objects.first(),
        'banners': HomeBanner.objects.filter(ativo=True),
        'destaques': PratoDestaque.objects.order_by('ordem'),
        'categorias': HomeCategoria.objects.prefetch_related('blocos').order_by('ordem'),
        'contatos': Contato.objects.all(),
        'horario': Horario.objects.first(),
        'promocoes': Promocao.objects.filter(ativo=True),
    }

"""

from django.db.models import Prefetch

def base_context():
    return {
        'site_info': SiteInfo.objects.first(),
        'slogans': Slogan.objects.first(),
        'banners': HomeBanner.objects.filter(ativo=True),
        'destaques': PratoDestaque.objects.order_by('ordem'),

        'categorias': HomeCategoria.objects
            .filter(ativo=True)
            .order_by('ordem')
            .prefetch_related(
                Prefetch(
                    'blocos',
                    queryset=HomeBloco.objects
                        .filter(ativo=True)
                        .order_by('ordem')
                )
            ),

        'contato': Contato.objects.first(),
        'horario': Horario.objects.first(),
        'promocoes': Promocao.objects.filter(ativo=True),
    }


# =======================
# HOME
# =======================
def home(request):
    context = base_context()
    return render(request, 'index.html', context)


# =======================
# PRATOS / CARDÁPIO
# =======================

"""
def pratos(request):
    context = base_context()
    context['categorias_pratos'] = CategoriaPrato.objects.filter(ativo=True)
    return render(request, 'pratos.html', context)
    
"""


# =======================
# PROMOÇÕES
# =======================
def promocoes(request):
    context = base_context()
    context['promocoes'] = Promocao.objects.filter(ativo=True)
    return render(request, 'promo.html', context)


# =======================
# CONTATOS
# =======================
def contatos(request):
    context = base_context()
    context['contato'] = Contato.objects.first()
    return render(request, 'contatos.html', context)
    
from django.shortcuts import render, get_object_or_404
from .models import SiteInfo, CategoriaPrato, Prato

# Lista todas as categorias
def pratos_categoria(request):
    context = {
        'site_info': SiteInfo.objects.first(),
        'categorias': CategoriaPrato.objects.filter(ativo=True),
    }
    return render(request, 'pratos_categoria.html', context)


# Lista pratos de uma categoria específica, máximo 10
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import CategoriaPrato, Prato, SiteInfo, Contato

def pratos(request, categoria_id):
    # Pega a categoria ou retorna 404 se não existir
    categoria = get_object_or_404(CategoriaPrato, id=categoria_id, ativo=True)
    
    # Lista de pratos ativos da categoria
    pratos_list = categoria.pratos.filter(ativo=True).order_by('ordem')
    
    # Paginador: 10 pratos por página
    paginator = Paginator(pratos_list, 10)
    page_number = request.GET.get('page')  # pega número da página pela URL
    pratos = paginator.get_page(page_number)

    # Contexto que será enviado para o template
    context = {
        'site_info': SiteInfo.objects.first(),
        'categoria': categoria,
        'pratos': pratos,                  # objetos paginados
        'categorias': CategoriaPrato.objects.filter(ativo=True),
        'contatos': Contato.objects.all(),
    }

    return render(request, 'pratos.html', context)
