from django.db import models

class Boleto(models.Model):
    # Field name made lowercase.
    reftran = models.CharField(db_column='refTran', max_length=17, unique=True)
    # Field name made lowercase.
    documentopessoa = models.CharField(db_column='documentoPessoa', max_length=14, blank=True, null=True)
    # Field name made lowercase.
    datavencimento = models.DateField(db_column='dataVencimento', blank=True, null=True)
    destino = models.CharField(max_length=14, blank=True, null=True)
    raw = models.TextField(blank=True, null=True)
    # Field name made lowercase.
    codigobarras = models.CharField(db_column='codigoBarras', max_length=54, blank=True, null=True)
    pago = models.IntegerField()
    valor = models.IntegerField()
    # Field name made lowercase.
    datapagamento = models.DateField(db_column='dataPagamento', blank=True, null=True)
    # Field name made lowercase.
    dataemissao = models.DateField(db_column='dataEmissao', blank=True, null=True)
    # Field name made lowercase.
    valordescontado = models.IntegerField(db_column='valorDescontado', blank=True, null=True)
    # Field name made lowercase.
    valorpago = models.IntegerField(db_column='valorPago', blank=True, null=True)
    # Field name made lowercase.
    datacompensacao = models.DateField(db_column='dataCompensacao', blank=True, null=True)
    # Field name made lowercase.
    valorfumcad = models.IntegerField(db_column='valorFUMCAD', blank=True, null=True)
    tempo = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        ordering = ['id']
        verbose_name = 'Boleto'
        verbose_name_plural = 'Boletos'



class Cidade(models.Model):
    nome = models.CharField(max_length=40)
    # Field name made lowercase.
    idconv = models.CharField(max_length=10)
    convenio = models.CharField(max_length=10)
    #patrocinador1 = models.CharField(max_length=150)
    # patrocinadorlink1 = models.CharField(db_column='patrocinadorLink1', max_length=150)  # Field name made lowercase.
    #patrocinador2 = models.CharField(max_length=150)
    # patrocinadorlink2 = models.CharField(db_column='patrocinadorLink2', max_length=150)  # Field name made lowercase.
    #patrocinador3 = models.CharField(max_length=150)
    # patrocinadorlink3 = models.CharField(db_column='patrocinadorLink3', max_length=150)  # Field name made lowercase.
    #patrocinador4 = models.CharField(max_length=150)
    # patrocinadorlink4 = models.CharField(db_column='patrocinadorLink4', max_length=150)  # Field name made lowercase.
    #patrocinador5 = models.CharField(max_length=150)
    # patrocinadorlink5 = models.CharField(db_column='patrocinadorLink5', max_length=150)  # Field name made lowercase.
    #patrocinador6 = models.CharField(max_length=150)
    # patrocinadorlink6 = models.CharField(db_column='patrocinadorLink6', max_length=150)  # Field name made lowercase.
    banner = models.CharField(max_length=255, blank=True, null=True)
    # Field name made lowercase.
    porcentagemfundo = models.IntegerField()
    # Field name made lowercase.
    possuiprojetos = models.IntegerField()

    class Meta:
        ordering = ['id']
        verbose_name = 'Cidade'
        verbose_name_plural = 'Cidades'


class Instituicao(models.Model):
    cnpj = models.CharField(max_length=14)
    senha = models.CharField(max_length=64)
    foto = models.CharField(max_length=150)
    logo = models.CharField(max_length=512, blank=True, null=True)
    nome = models.CharField(max_length=75)
    descricao = models.CharField(max_length=5000, blank=True, null=True)
    endereco = models.CharField(max_length=50, blank=True, null=True)
    telefone = models.CharField(max_length=11, blank=True, null=True)
    whatsapp = models.CharField(max_length=12, blank=True, null=True)
    publico = models.CharField(max_length=5000, blank=True, null=True)
    acoes = models.CharField(max_length=5000, blank=True, null=True)
    dimensionamento = models.CharField(max_length=5000, blank=True, null=True)
    pretencoes = models.CharField(max_length=5000, blank=True, null=True)
    # Field name made lowercase.
    porquedoar = models.CharField(db_column='porqueDoar', max_length=5000, blank=True, null=True)
    sigla = models.CharField(max_length=50)
    site = models.CharField(max_length=100, blank=True, null=True)
    facebook = models.CharField(max_length=100, blank=True, null=True)
    permissoes = models.IntegerField()
    ativo = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    # Field name made lowercase.
    idcidade = models.IntegerField(db_column='idCidade')
    # Field name made lowercase.
    projetodatainicio = models.DateField(db_column='projetoDataInicio', blank=True, null=True)
    # Field name made lowercase.
    projetodataencerramento = models.DateField(db_column='projetoDataEncerramento', blank=True, null=True)
    # Field name made lowercase.
    projetometaarrecadacao = models.IntegerField(db_column='projetoMetaArrecadacao', blank=True, null=True)
    login = models.CharField(max_length=20, unique=True)

    class Meta:
        ordering = ['id']
        verbose_name = 'Instituição'
        verbose_name_plural = 'Instituições'


class Pessoa(models.Model):
    documento = models.CharField(unique=True, max_length=14)
    senha = models.CharField(max_length=64)
    # Field name made lowercase.
    tipodocumento = models.IntegerField(db_column='tipoDocumento')
    nome = models.CharField(max_length=50)
    email = models.CharField(max_length=40, blank=True, null=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    cep = models.CharField(max_length=8)
    logradouro = models.CharField(max_length=60)
    cidade = models.CharField(max_length=50)
    bairro = models.CharField(max_length=30)
    numero = models.CharField(max_length=5)
    complemento = models.CharField(max_length=20, blank=True, null=True)
    uf = models.CharField(max_length=2)

    class Meta:
        ordering = ['id']
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'


class Patrocinador (models.Model):
    cnpj = models.CharField(max_length=14)
    senha = models.CharField(max_length=64)
    foto = models.CharField(max_length=150)
    logo = models.CharField(max_length=512, blank=True, null=True)
    nome = models.CharField(max_length=75)
    descricao = models.CharField(max_length=5000, blank=True, null=True)
    endereco = models.CharField(max_length=50, blank=True, null=True)
    telefone = models.CharField(max_length=11, blank=True, null=True)
    whatsapp = models.CharField(max_length=12, blank=True, null=True)

    class Meta:
        ordering = ['id']
        verbose_name = 'Patrocinador'
        verbose_name_plural = 'Patrocinadores'    


class Patrocinador_Cidade (models.Model):
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    patrocinador = models.ForeignKey(Patrocinador, on_delete=models.CASCADE)
    link = models.CharField(max_length=150)

    class Meta:
        ordering = ['id']
        verbose_name = 'Patrocinador_Cidade'
        verbose_name_plural = 'Patrocinadores_Cidades'    

