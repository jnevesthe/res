from django.shortcuts import render, redirect

from django.views.generic import TemplateView, ListView, DetailView, UpdateView

from loja.models import HomeCategoria, SobreCategoria, HomeBloco, SobreBloco, Contato, GaleriaCategoria, BlocoGaleria, CategoriaPrato, Prato, PratoDestaque, SiteInfo, Slogan, HomeBanner, Horario, Promocao, SobreCategoria, SobreBloco


from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy

def login_view(request):
  if( request.method == "POST"):
    username=request.POST.get("username")
    password=request.POST.get("password")
    
    user=authenticate(username=username, password=password)
    
    if(user):
      login(request, user)
      return redirect("painel:painel")
    else:
      error="Usúarios ou Senhas erradas!"
  else:
    error="Preencha tudo!"
  return render(request, 'painel/Login.html', {'error':error})    
  
def logout_view(request):
  try:
    logout(request)
    print('OK')
    return redirect('painel:login')
  except:
    return redirect('painel:login')
  

    
                
class Painel(TemplateView):
    template_name="painel/base.html"
    

class HomeCategoriaListView(ListView):
    model = HomeCategoria
    template_name = "painel/categoria_home_list.html"
    #template_name='painel/h.html'
    context_object_name = "categorias"
    ordering = ["ordem"]
    
class ContatosListView(ListView):
    model = Contato
    template_name = "painel/contatos_list.html"
    context_object_name = "contatos"
    
class ContatosDetailView(DetailView):
    model = Contato
    template_name = "painel/contatos_detail.html"
    context_object_name = "contato"
    
class ContatosUpdateView(UpdateView):
    model = Contato
    fields = '__all__'
    template_name = "painel/contatos_edit.html"
    #context_object_name = "contato" 
    success_url = reverse_lazy('painel:contatos-list')

class HomeBlocoListView(ListView):
    model = HomeBloco
    template_name = "painel/bloco_list.html"
    context_object_name = "blocos"

    def get_queryset(self):
        return HomeBloco.objects.filter(categoria_id=self.kwargs["categoria_id"]).order_by("ordem")

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["categoria"] = HomeCategoria.objects.get(id=self.kwargs["categoria_id"])
        return ctx


class HomeCategoriasUpdateView(UpdateView):
    model = HomeCategoria
    fields = "__all__"
    template_name = "painel/form.html"

    def get_success_url(self):
        return reverse_lazy("painel:home-blocos", kwargs={"categoria_id": self.object.categoria.id})



class HomeBlocoUpdateView(UpdateView):
    model = HomeBloco
    fields = "__all__"
    template_name = "painel/form.html"

    def get_success_url(self):
        return reverse_lazy("painel:home-blocos", kwargs={"categoria_id": self.object.categoria.id})

class HomeCategoriaDetailView(DetailView):
    model = HomeCategoria
    template_name = "painel/detail.html"

class HomeBlocoDetailView(DetailView):
    model = HomeBloco
    template_name = "painel/bloco_detail.html"
    context_object_name = "bloco"
    
    

class GaleriaCategoriaListView(ListView):
    model = GaleriaCategoria
    template_name = "painel/galeria/categoria_list.html"
    context_object_name = "categorias"

class GaleriaBlocoListView(ListView):
    model = BlocoGaleria
    template_name = "painel/galeria/bloco_list.html"
    context_object_name = "blocos"

    def get_queryset(self):
        return BlocoGaleria.objects.filter(categoria_id=self.kwargs["categoria_id"])
        
class GaleriaCategoriaUpdateView(UpdateView):
    model = GaleriaCategoria
    fields = '__all__'
    template_name = "painel/galeria/categoria_list.html"


class GaleriaBlocoUpdateView(UpdateView):
    model = BlocoGaleria
    fields = "__all__"
    template_name = "painel/form.html"

    def get_success_url(self):
        return reverse_lazy("painel:galeria-blocos", kwargs={"categoria_id": self.object.categoria.id})    
        
class GaleriaCategoriaDetailView(DetailView):
    model = GaleriaCategoria
    template_name = "painel/galeria/categoria_detail.html"    
    
class GaleriaBlocoDetailView(DetailView):
    model = BlocoGaleria
    template_name = "painel/galeria/bloco_detail.html"    
    
    

# =======================
# CATEGORIAS DE PRATOS
# =======================

class CategoriaPratoListView(ListView):
    model = CategoriaPrato
    template_name = "painel/pratos/categoria_list.html"
    context_object_name = "categorias"


class CategoriaPratoDetailView(DetailView):
    model = CategoriaPrato
    template_name = "painel/pratos/categoria_detail.html"
    context_object_name = "categoria"


class CategoriaPratoUpdateView(UpdateView):
    model = CategoriaPrato
    fields = "__all__"
    template_name = "painel/form.html"
    success_url = reverse_lazy("painel:categoria-prato-list")


# =======================
# PRATOS
# =======================

class PratoListPorCategoriaView(ListView):
    model = Prato
    template_name = "painel/pratos/prato_list.html"
    context_object_name = "pratos"

    def get_queryset(self):
        return Prato.objects.filter(
            categoria_id=self.kwargs["categoria_id"]
        ).order_by("ordem")

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["categoria"] = CategoriaPrato.objects.get(
            id=self.kwargs["categoria_id"]
        )
        return ctx

class PratoDetailView(DetailView):
    model = Prato
    template_name = "painel/pratos/prato_detail.html"
    context_object_name = "prato"


class PratoUpdateView(UpdateView):
    model = Prato
    fields = "__all__"
    template_name = "painel/form.html"
    success_url = reverse_lazy("painel:pratos-list")


# =======================
# PRATOS EM DESTAQUE
# =======================

class PratoDestaqueListView(ListView):
    model = PratoDestaque
    template_name = "painel/pratos/prato_destaque_list.html"
    context_object_name = "pratos"
    ordering = ["ordem"]


class PratoDestaqueDetailView(DetailView):
    model = PratoDestaque
    template_name = "painel/pratos/prato_destaque_detail.html"
    context_object_name = "prato"


class PratoDestaqueUpdateView(UpdateView):
    model = PratoDestaque
    fields = "__all__"
    template_name = "painel/form.html"
    success_url = reverse_lazy("painel:pratos-destaque-list")    
        

# =======================
# SITE INFO
# =======================
class SiteInfoListView(ListView):
    model = SiteInfo
    template_name = "painel/info/siteinfo_list.html"
    context_object_name = "infos"

class SiteInfoDetailView(DetailView):
    model = SiteInfo
    template_name = "painel/info/siteinfo_detail.html"
    context_object_name = "info"

class SiteInfoUpdateView(UpdateView):
    model = SiteInfo
    fields = "__all__"
    template_name = "painel/form.html"
    success_url = reverse_lazy("painel:siteinfo-list")


# =======================
# SLOGAN
# =======================
class SloganListView(ListView):
    model = Slogan
    template_name = "painel/info/slogan_list.html"
    context_object_name = "slogans"

class SloganDetailView(DetailView):
    model = Slogan
    template_name = "painel/info/slogan_detail.html"
    context_object_name = "slogan"

class SloganUpdateView(UpdateView):
    model = Slogan
    fields = "__all__"
    template_name = "painel/form.html"
    success_url = reverse_lazy("painel:slogan-list")


# =======================
# HOME BANNER
# =======================
class HomeBannerListView(ListView):
    model = HomeBanner
    template_name = "painel/info/homebanner_list.html"
    context_object_name = "banners"
    ordering = ["id"]

class HomeBannerDetailView(DetailView):
    model = HomeBanner
    template_name = "painel/info/homebanner_detail.html"
    context_object_name = "banner"

class HomeBannerUpdateView(UpdateView):
    model = HomeBanner
    fields = "__all__"
    template_name = "painel/form.html"
    success_url = reverse_lazy("painel:homebanner-list")     
    
    

# =======================
# HORÁRIOS
# =======================
class HorarioListView(ListView):
    model = Horario
    template_name = "painel/horarios/horario_list.html"
    context_object_name = "horarios"

class HorarioDetailView(DetailView):
    model = Horario
    template_name = "painel/horarios/horario_detail.html"
    context_object_name = "horario"

class HorarioUpdateView(UpdateView):
    model = Horario
    fields = "__all__"
    template_name = "painel/form.html"
    success_url = reverse_lazy("painel:horario-list")


# =======================
# PROMOÇÕES
# =======================
class PromocaoListView(ListView):
    model = Promocao
    template_name = "painel/promocoes/promocao_list.html"
    context_object_name = "promocoes"
    ordering = ["ordem"]

class PromocaoDetailView(DetailView):
    model = Promocao
    template_name = "painel/promocoes/promocao_detail.html"
    context_object_name = "promocao"

class PromocaoUpdateView(UpdateView):
    model = Promocao
    fields = "__all__"
    template_name = "painel/form.html"
    success_url = reverse_lazy("painel:promocao-list")    



# =======================
# SOBRE CATEGORIAS
# =======================
class SobreCategoriaListView(ListView):
    model = SobreCategoria
    template_name = "painel/sobre/categoria_list.html"
    context_object_name = "categorias"

class SobreCategoriaDetailView(DetailView):
    model = SobreCategoria
    template_name = "painel/sobre/categoria_detail.html"
    context_object_name = "categoria"

class SobreCategoriaUpdateView(UpdateView):
    model = SobreCategoria
    fields = "__all__"
    template_name = "painel/form.html"
    success_url = reverse_lazy("painel:sobre-categorias-list")


# =======================
# SOBRE BLOCOS (por categoria)
# =======================
class SobreBlocoListView(ListView):
    model = SobreBloco
    template_name = "painel/sobre/bloco_list.html"
    context_object_name = "blocos"

    def get_queryset(self):
        return SobreBloco.objects.filter(categoria_id=self.kwargs["categoria_id"]).order_by("ordem")

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["categoria"] = SobreCategoria.objects.get(id=self.kwargs["categoria_id"])
        return ctx


class SobreBlocoDetailView(DetailView):
    model = SobreBloco
    template_name = "painel/sobre/bloco_detail.html"
    context_object_name = "bloco"


class SobreBlocoUpdateView(UpdateView):
    model = SobreBloco
    fields = "__all__"
    template_name = "painel/form.html"

    def get_success_url(self):
        return reverse_lazy(
            "painel:sobre-blocos",
            kwargs={"categoria_id": self.object.categoria.id}
        )    
    