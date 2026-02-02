from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.shortcuts import redirect
from .models import (
    SiteInfo, Slogan, HomeBanner, Contato,
    HomeCategoria, HomeBloco, CategoriaPrato,
    Prato, PratoDestaque, Horario, Promocao,
    SobreCategoria, SobreBloco
)

APP_NAME = 'loja' 

# =================================================================
# 1. ADMINS DE EDIÇÃO COMPLETA (FORMULÁRIOS)
# =================================================================

@admin.register(HomeBloco)
class HomeBlocoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'categoria', 'ordem', 'ativo')
    list_filter = ('categoria', 'ativo')
    search_fields = ('nome', 'titulo')
    save_on_top = True
    
    fieldsets = (
        ("Identificação", {'fields': ('categoria', 'nome', 'ordem', 'ativo')}),
        ("Conteúdo Principal", {'fields': ('titulo', 'texto')}),
        ("Links e Botões", {'fields': (('link_url', 'link_texto', 'botao_url', 'botao_texto'),)}),
        ("Imagem", {'fields': (('imagem', 'imagem_texto'),)}),
    )

    def response_add(self, request, obj, post_url_continue=None):
        return redirect(f'/admin/{APP_NAME}/homecategoria/{obj.categoria.id}/change/')

    def response_change(self, request, obj):
        return redirect(f'/admin/{APP_NAME}/homecategoria/{obj.categoria.id}/change/')


@admin.register(SobreBloco)
class SobreBlocoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'categoria', 'ordem', 'ativo')
    save_on_top = True
    
    fieldsets = (
        ("Identificação", {'fields': ('categoria', 'nome', 'ordem', 'ativo')}),
        ("Conteúdo Principal", {'fields': ('titulo', 'texto')}),
        ("Links e Botões", {'fields': (('link_url', 'link_texto', 'botao_url', 'botao_texto'),)}),
        ("Imagem", {'fields': (('imagem', 'imagem_texto'),)}),
    )

    def response_add(self, request, obj, post_url_continue=None):
        return redirect(f'/admin/{APP_NAME}/sobrecategoria/{obj.categoria.id}/change/')

    def response_change(self, request, obj):
        return redirect(f'/admin/{APP_NAME}/sobrecategoria/{obj.categoria.id}/change/')


@admin.register(Prato)
class PratoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'categoria', 'ordem', 'preco', 'ativo')
    
    def response_add(self, request, obj, post_url_continue=None):
        return redirect(f'/admin/{APP_NAME}/categoriaprato/{obj.categoria.id}/change/')

    def response_change(self, request, obj):
        return redirect(f'/admin/{APP_NAME}/categoriaprato/{obj.categoria.id}/change/')


# =================================================================
# 2. INLINES (ÍNDICE DENTRO DAS CATEGORIAS)
# =================================================================

class HomeBlocoInline(admin.TabularInline):
    model = HomeBloco
    fields = ('contagem', 'nome', 'ordem', 'ativo', 'link_editar') 
    readonly_fields = ('contagem', 'link_editar')
    extra = 0
    ordering = ('ordem',)

    def contagem(self, obj):
        if obj.id:
            blocos = list(obj.categoria.blocos.all().order_by('ordem', 'id'))
            return format_html("<b>Bloco {}</b>", blocos.index(obj) + 1)
        return "Novo"
    contagem.short_description = "Nº"

    def link_editar(self, obj):
        if obj.id:
            url = reverse(f'admin:{APP_NAME}_homebloco_change', args=[obj.id])
            return format_html('<a href="{}" style="font-weight:bold; color:#447e9b;">Editar</a>', url)
        return "-"


class SobreBlocoInline(admin.TabularInline):
    model = SobreBloco
    fields = ('contagem', 'nome', 'ordem', 'ativo', 'link_editar')
    readonly_fields = ('contagem', 'link_editar')
    extra = 0
    ordering = ('ordem',)

    def contagem(self, obj):
        if obj.id:
            blocos = list(obj.categoria.blocos.all().order_by('ordem', 'id'))
            return format_html("<b>Bloco {}</b>", blocos.index(obj) + 1)
        return "Novo"

    def link_editar(self, obj):
        if obj.id:
            url = reverse(f'admin:{APP_NAME}_sobrebloco_change', args=[obj.id])
            return format_html('<a href="{}" style="font-weight:bold; color:#447e9b;">Editar</a>', url)
        return "-"


class PratoInline(admin.TabularInline):
    model = Prato
    fields = ('contagem', 'nome', 'preco', 'ativo', 'link_editar')
    readonly_fields = ('contagem', 'link_editar')
    extra = 0
    ordering = ('ordem',)

    def contagem(self, obj):
        if obj.id:
            pratos = list(obj.categoria.pratos.all().order_by('ordem', 'id'))
            return format_html("<b>Prato {}</b>", pratos.index(obj) + 1)
        return "Novo"

    def link_editar(self, obj):
        if obj.id:
            url = reverse(f'admin:{APP_NAME}_prato_change', args=[obj.id])
            return format_html('<a href="{}" style="font-weight:bold; color:#447e9b;">Editar</a>', url)
        return "-"


# =================================================================
# 3. ADMINS PAIS (CATEGORIAS)
# =================================================================

@admin.register(HomeCategoria)
class HomeCategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ordem', 'ativo')
    inlines = [HomeBlocoInline]
    readonly_fields = ('btn_add',)

    def btn_add(self, obj):
        if obj.id:
            url = reverse(f'admin:{APP_NAME}_homebloco_add') + f'?categoria={obj.id}'
            return format_html(
                '<a class="addlink" style="background:#417690; color:white; padding:10px; border-radius:4px; text-decoration:none; font-weight:bold;" href="{}">＋ ADICIONAR NOVO BLOCO</a>',
                url
            )
        return "Salve a categoria primeiro."


@admin.register(SobreCategoria)
class SobreCategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ordem', 'ativo')
    inlines = [SobreBlocoInline]
    readonly_fields = ('btn_add',)

    def btn_add(self, obj):
        if obj.id:
            url = reverse(f'admin:{APP_NAME}_sobrebloco_add') + f'?categoria={obj.id}'
            return format_html(
                '<a class="addlink" style="background:#417690; color:white; padding:10px; border-radius:4px; text-decoration:none; font-weight:bold;" href="{}">＋ ADICIONAR NOVO BLOCO</a>',
                url
            )
        return "Salve primeiro."


@admin.register(CategoriaPrato)
class CategoriaPratoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ativo')
    list_editable = ('ativo',) 
    inlines = [PratoInline]
    readonly_fields = ('btn_add',)

    def btn_add(self, obj):
        if obj.id:
            url = reverse(f'admin:{APP_NAME}_prato_add') + f'?categoria={obj.id}'
            return format_html(
                '<a class="addlink" style="background:#417690; color:white; padding:10px; border-radius:4px; text-decoration:none; font-weight:bold;" href="{}">＋ ADICIONAR NOVO PRATO</a>',
                url
            )
        return "Salve primeiro."


# =================================================================
# 4. RESTANTE (MODELOS SIMPLES)
# =================================================================
admin.site.register([SiteInfo, Slogan, Contato, Horario, HomeBanner, Promocao, PratoDestaque])


from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.shortcuts import redirect
from .models import GaleriaCategoria, BlocoGaleria

APP_NAME = 'loja'

# =========================
# Inline dos blocos da galeria
# =========================
class BlocoGaleriaInline(admin.TabularInline):
    model = BlocoGaleria
    fields = ('contagem', 'imagem', 'legenda', 'ordem', 'ativo', 'link_editar')
    readonly_fields = ('contagem', 'link_editar')
    extra = 0
    show_change_link = True
    ordering = ('ordem',)

    def contagem(self, obj):
        if obj.id:
            blocos = list(obj.categoria.blocos.all().order_by('ordem', 'id'))
            return format_html("<b>Bloco {}</b>", blocos.index(obj) + 1)
        return "Novo"

    def link_editar(self, obj):
        if obj.id:
            url = reverse(f'admin:{APP_NAME}_blocogaleria_change', args=[obj.id])
            return format_html('<a href="{}" style="font-weight:bold; color:#447e9b;">Editar</a>', url)
        return "-"

# =========================
# Admin da Categoria Galeria
# =========================
@admin.register(GaleriaCategoria)
class GaleriaCategoriaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'ordem', 'ativo')
    list_editable = ('ordem', 'ativo')
    inlines = [BlocoGaleriaInline]
    search_fields = ('titulo',)
    readonly_fields = ('btn_add',)

    def btn_add(self, obj):
        if obj.id:
            url = reverse(f'admin:{APP_NAME}_blocogaleria_add') + f'?categoria={obj.id}'
            return format_html(
                '<a class="addlink" style="background:#417690; color:white; padding:10px; '
                'border-radius:4px; text-decoration:none; font-weight:bold;" href="{}">'
                '＋ ADICIONAR NOVO BLOCO</a>', url
            )
        return "Salve a categoria primeiro."

# =========================
# Admin dos Blocos Galeria
# =========================
@admin.register(BlocoGaleria)
class BlocoGaleriaAdmin(admin.ModelAdmin):
    list_display = ('categoria', 'legenda', 'ordem', 'ativo')
    list_filter = ('categoria', 'ativo')
    ordering = ('categoria', 'ordem')
    search_fields = ('legenda',)

    def response_add(self, request, obj, post_url_continue=None):
        return redirect(f'/admin/{APP_NAME}/galeriacategoria/{obj.categoria.id}/change/')

    def response_change(self, request, obj):
        return redirect(f'/admin/{APP_NAME}/galeriacategoria/{obj.categoria.id}/change/')
