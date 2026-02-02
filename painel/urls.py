from django.urls import path
from .views import *

app_name = "painel"

urlpatterns = [
    # =======================
    # LOGIN / LOGOUT
    # =======================
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),

    # =======================
    # PAINEL
    # =======================
    path("", Painel.as_view(), name="painel"),

    # =======================
    # CONTATOS
    # =======================
    path("contatos/", ContatosListView.as_view(), name="contatos-list"),
    path("contatos/<int:pk>/", ContatosDetailView.as_view(), name="contatos-detail"),
    path("contatos/edit/<int:pk>/", ContatosUpdateView.as_view(), name="contatos-edit"),

    # =======================
    # HOME
    # =======================
    path("home/", HomeCategoriaListView.as_view(), name="home-categorias"),
    path("home/<int:categoria_id>/", HomeBlocoListView.as_view(), name="home-blocos"),
    path("home/categoria/edit/<int:pk>/", HomeCategoriasUpdateView.as_view(), name="home-categorias-edit"),
    path("home/bloco/edit/<int:pk>/", HomeBlocoUpdateView.as_view(), name="home-bloco-edit"),
    path("home/categoria/detail/<int:pk>/", HomeCategoriaDetailView.as_view(), name="home-categorias-detail"),
    path("home/bloco/<int:pk>/detail/", HomeBlocoDetailView.as_view(), name="home-bloco-detail"),

    # =======================
    # GALERIA
    # =======================
    path("galeria/", GaleriaCategoriaListView.as_view(), name="galeria-categorias"),
    path("galeria/<int:categoria_id>/", GaleriaBlocoListView.as_view(), name="galeria-blocos"),
    path("galeria/categoria/edit/<int:pk>/", GaleriaCategoriaUpdateView.as_view(), name="galeria-categorias-edit"),
    path("galeria/categoria/detail/<int:pk>/", GaleriaCategoriaDetailView.as_view(), name="galeria-categorias-detail"),
    path("galeria/bloco/edit/<int:pk>/", GaleriaBlocoUpdateView.as_view(), name="galeria-bloco-edit"),
    path("galeria/bloco/<int:pk>/detail/", GaleriaBlocoDetailView.as_view(), name="galeria-bloco-detail"),

    # =======================
    # CATEGORIAS DE PRATOS
    # =======================
    path("pratos/categorias/", CategoriaPratoListView.as_view(), name="categoria-prato-list"),
    path("pratos/categorias/<int:pk>/", CategoriaPratoDetailView.as_view(), name="categoria-prato-detail"),
    path("pratos/categorias/edit/<int:pk>/", CategoriaPratoUpdateView.as_view(), name="categoria-prato-edit"),

    # =======================
    # PRATOS POR CATEGORIA
    # =======================
    path("pratos/categoria/<int:categoria_id>/", PratoListPorCategoriaView.as_view(), name="pratos-por-categoria"),

    # =======================
    # PRATOS
    # =======================
    #path("pratos/", PratoListView.as_view(), name="pratos-list"),
    path("pratos/<int:pk>/", PratoDetailView.as_view(), name="pratos-detail"),
    path("pratos/edit/<int:pk>/", PratoUpdateView.as_view(), name="pratos-edit"),

    # =======================
    # PRATOS EM DESTAQUE
    # =======================
    path("pratos-destaque/", PratoDestaqueListView.as_view(), name="pratos-destaque-list"),
    path("pratos-destaque/<int:pk>/", PratoDestaqueDetailView.as_view(), name="pratos-destaque-detail"),
    path("pratos-destaque/edit/<int:pk>/", PratoDestaqueUpdateView.as_view(), name="pratos-destaque-edit"),
    
    # =======================
    # SITE INFO
    # =======================
    path("info/", SiteInfoListView.as_view(), name="siteinfo-list"),
    path("info/<int:pk>/", SiteInfoDetailView.as_view(), name="siteinfo-detail"),
    path("info/edit/<int:pk>/", SiteInfoUpdateView.as_view(), name="siteinfo-edit"),

# =======================
# SLOGAN
# =======================
    path("slogans/", SloganListView.as_view(), name="slogan-list"),
    path("slogans/<int:pk>/", SloganDetailView.as_view(), name="slogan-detail"),
    path("slogans/edit/<int:pk>/", SloganUpdateView.as_view(), name="slogan-edit"),

# =======================
# HOME BANNER
# =======================
    path("homebanner/", HomeBannerListView.as_view(), name="homebanner-list"),
    path("homebanner/<int:pk>/", HomeBannerDetailView.as_view(), name="homebanner-detail"),
    path("homebanner/edit/<int:pk>/", HomeBannerUpdateView.as_view(), name="homebanner-edit"),
    
  
    # =======================
# HORÁRIOS
# =======================
    path("horarios/", HorarioListView.as_view(), name="horario-list"),
    path("horarios/<int:pk>/", HorarioDetailView.as_view(), name="horario-detail"),
    path("horarios/edit/<int:pk>/", HorarioUpdateView.as_view(), name="horario-edit"),

# =======================
# PROMOÇÕES
# =======================
    path("promocoes/", PromocaoListView.as_view(), name="promocao-list"),
    path("promocoes/<int:pk>/", PromocaoDetailView.as_view(), name="promocao-detail"),
    path("promocoes/edit/<int:pk>/", PromocaoUpdateView.as_view(), name="promocao-edit"), 
    
    
    # =======================
# SOBRE CATEGORIAS
# =======================
    path("sobre/categorias/", SobreCategoriaListView.as_view(), name="sobre-categorias-list"),
    path("sobre/categorias/<int:pk>/", SobreCategoriaDetailView.as_view(), name="sobre-categorias-detail"),
    path("sobre/categorias/edit/<int:pk>/", SobreCategoriaUpdateView.as_view(), name="sobre-categorias-edit"),

# =======================
# SOBRE BLOCOS (por categoria)
# =======================
    path("sobre/<int:categoria_id>/blocos/", SobreBlocoListView.as_view(), name="sobre-blocos"),
    path("sobre/bloco/<int:pk>/detail/", SobreBlocoDetailView.as_view(), name="sobre-bloco-detail"),
    path("sobre/bloco/edit/<int:pk>/", SobreBlocoUpdateView.as_view(), name="sobre-bloco-edit"),    
  
    
]