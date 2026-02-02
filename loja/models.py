from django.db import models

# =======================
# Informações do site
# =======================
class SiteInfo(models.Model):
    nome = models.CharField(
        max_length=150,
        help_text="Nome do restaurante ou site"
    )
    logo = models.ImageField(
        upload_to='info/',
        help_text="Logotipo do restaurante"
    )

    def __str__(self):
        return self.nome


class Slogan(models.Model):
    slogan = models.CharField(
        max_length=350,
        help_text="Frase curta de impacto exibida no site"
    )

    def __str__(self):
        return self.slogan


# =======================
# Banner da página inicial
# =======================
class HomeBanner(models.Model):
    titulo = models.CharField(
        max_length=100,
        help_text="Título principal do banner"
    )
    texto = models.TextField(
        blank=True,
        help_text="Texto complementar do banner"
    )
    imagem = models.ImageField(
        upload_to='home/',
        blank=True,
        help_text="Imagem do banner"
    )
    link = models.CharField(
        blank=True,
        max_length=250,
        help_text="Link do banner"
    )
    texto_link = models.CharField(
        blank=True,
        max_length=35,
        help_text="Texto do botão/link do banner"
    )
    ativo = models.BooleanField(
        default=True,
        help_text="Marque para exibir no site"
    )

    def __str__(self):
        return self.titulo


# =======================
# Contatos
# =======================
class Contato(models.Model):
    telefone = models.CharField(
        max_length=20,
        blank=True,
        help_text="Telefone principal"
    )
    telefone2 = models.CharField(
        max_length=20,
        blank=True,
        help_text="Telefone secundário"
    )
    email = models.EmailField(
        blank=True,
        help_text="Email de contato"
    )
    whatsapp = models.CharField(
        max_length=20,
        blank=True,
        help_text="Número do WhatsApp"
    )
    insta = models.CharField(
        max_length=100,
        blank=True,
        help_text="Instagram (@usuario)"
    )

    def __str__(self):
        return self.telefone or self.email or "Contato"


# =======================
# Categorias e Blocos HOME
# =======================
class HomeCategoria(models.Model):
    nome = models.CharField(
        max_length=100,
        help_text="Nome da categoria da home"
    )
    ordem = models.IntegerField(
        default=0,
        help_text="Ordem de exibição"
    )
    
    ativo = models.BooleanField(default=True, help_text="Bloco ativo")

    def __str__(self):
        return self.nome



class HomeBloco(models.Model):
    categoria = models.ForeignKey(
        HomeCategoria,
        on_delete=models.CASCADE,
        related_name='blocos'
    )

    nome = models.CharField(max_length=100, blank=True)
    titulo = models.CharField(max_length=150, blank=True)

    # TEXTO
    texto = models.TextField(blank=True)

    # LINK
    link_url = models.CharField(max_length=250, blank=True)
    link_texto = models.CharField(max_length=250, blank=True)

    # BOTÃO
    botao_url = models.CharField(max_length=250, blank=True)
    botao_texto = models.CharField(max_length=250, blank=True)

    # IMAGEM
    imagem = models.ImageField(upload_to='home/', blank=True)
    imagem_texto = models.CharField(max_length=150, blank=True)

    ordem = models.IntegerField(default=0)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome or self.titulo or "Bloco Home"


# =======================
# Pratos
# =======================
class CategoriaPrato(models.Model):
    nome = models.CharField(max_length=100, help_text="Nome da categoria")
    ativo = models.BooleanField(default=True, help_text="Categoria ativa")
    

    def __str__(self):
        return self.nome


class Prato(models.Model):
    categoria = models.ForeignKey(
        CategoriaPrato,
        on_delete=models.CASCADE,
        related_name='pratos'
    )
    nome = models.CharField(max_length=100, help_text="Nome do prato")
    ordem = models.IntegerField(default=0, help_text="Ordem de exibição")
    descricao = models.TextField(blank=True, help_text="Descrição do prato")
    preco = models.DecimalField(max_digits=8, decimal_places=2, help_text="Preço")
    imagem = models.ImageField(upload_to='pratos/', blank=True, help_text="Imagem do prato")
    ativo = models.BooleanField(default=True, help_text="Disponível no cardápio")
    vegetariano = models.BooleanField(default=False, help_text="Prato vegetariano")

    def __str__(self):
        return self.nome


class PratoDestaque(models.Model):
    nome = models.CharField(max_length=100, help_text="Nome do prato em destaque")
    descricao = models.TextField(blank=True, help_text="Descrição")
    preco = models.DecimalField(max_digits=8, decimal_places=2, help_text="Preço")
    imagem = models.ImageField(upload_to='pratos/', blank=True, help_text="Imagem")
    ordem = models.IntegerField(default=0, help_text="Ordem de exibição")

    def __str__(self):
        return self.nome


# =======================
# Horários
# =======================
class Horario(models.Model):
    abertura_seg_sex = models.TimeField(help_text="Abertura (Seg–Sex)")
    fechamento_seg_sex = models.TimeField(help_text="Fechamento (Seg–Sex)")
    abertura_sab = models.TimeField(help_text="Abertura Sábado")
    fechamento_sab = models.TimeField(help_text="Fechamento Sábado")
    abertura_dom = models.TimeField(help_text="Abertura Domingo")
    fechamento_dom = models.TimeField(help_text="Fechamento Domingo")
    abertura_feriado = models.TimeField(null=True, blank=True, help_text="Abertura Feriado")
    fechamento_feriado = models.TimeField(null=True, blank=True, help_text="Fechamento Feriado")

    def __str__(self):
        return "Horário do Restaurante"


# =======================
# Promoções
# =======================
class Promocao(models.Model):
    titulo = models.CharField(max_length=100, help_text="Título da promoção")
    descricao = models.TextField(blank=True, help_text="Descrição ou regras")
    imagem = models.ImageField(upload_to='promocoes/', blank=True, null=True, help_text="Imagem da promoção")
    tag_desconto = models.CharField(max_length=20, blank=True, help_text="Ex: 20% OFF")
    ativo = models.BooleanField(default=True, help_text="Promoção ativa")
    ordem = models.IntegerField(default=0, help_text="Ordem de exibição")
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['ordem']

    def __str__(self):
        return self.titulo


# =======================
# SOBRE
# =======================
class SobreCategoria(models.Model):
    nome = models.CharField(max_length=100, help_text="Nome da categoria")
    ordem = models.IntegerField(default=0, help_text="Ordem")
    ativo = models.BooleanField(default=True, help_text="Ativo")

    class Meta:
        ordering = ["ordem"]

    def __str__(self):
        return self.nome

class SobreBloco(models.Model):
    categoria = models.ForeignKey(
        SobreCategoria,
        on_delete=models.CASCADE,
        related_name="blocos"
    )

    nome = models.CharField(max_length=100, blank=True)
    titulo = models.CharField(max_length=150, blank=True)

    # TEXTO
    texto = models.TextField(blank=True)

    # LINK
    link_url = models.CharField(max_length=250, blank=True)
    link_texto = models.CharField(max_length=250, blank=True)

    # BOTÃO
    botao_url = models.CharField(max_length=250, blank=True)
    botao_texto = models.CharField(max_length=250, blank=True)

    # IMAGEM
    imagem = models.ImageField(upload_to="sobre/", blank=True)
    imagem_texto = models.CharField(max_length=150, blank=True)

    ordem = models.IntegerField(default=0)
    ativo = models.BooleanField(default=True)

    class Meta:
        ordering = ["ordem"]

    def __str__(self):
        return self.nome or "Bloco Sobre"



class GaleriaCategoria(models.Model):
    titulo = models.CharField(max_length=150, help_text="Título da galeria")
    ordem = models.IntegerField(default=0, help_text="Ordem de exibição")
    ativo = models.BooleanField(default=True)

    class Meta:
        ordering = ['ordem']

    def __str__(self):
        return self.titulo


class BlocoGaleria(models.Model):
    categoria = models.ForeignKey(
        GaleriaCategoria,
        on_delete=models.CASCADE,
        related_name='blocos'
    )
    nome = models.CharField(max_length=150, blank=True, help_text="nome apenas para identificação")
    imagem = models.ImageField(upload_to='galeria/', help_text="Imagem da galeria")
    imagem_texto = models.CharField(max_length=150, blank=True, help_text="Legenda da imagem")
    legenda = models.CharField(max_length=150, blank=True, help_text="Legenda da imagem")
    ordem = models.IntegerField(default=0, help_text="Ordem do bloco")
    ativo = models.BooleanField(default=True)

    class Meta:
        ordering = ['ordem']

    def __str__(self):
        return self.legenda or f"Imagem {self.id}"
