# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Boleto(models.Model):
    reftran = models.CharField(db_column='refTran', primary_key=True, max_length=17)  # Field name made lowercase.
    documentopessoa = models.CharField(db_column='documentoPessoa', max_length=14, blank=True, null=True)  # Field name made lowercase.
    datavencimento = models.DateField(db_column='dataVencimento', blank=True, null=True)  # Field name made lowercase.
    destino = models.CharField(max_length=14, blank=True, null=True)
    raw = models.TextField(blank=True, null=True)
    codigobarras = models.CharField(db_column='codigoBarras', max_length=54, blank=True, null=True)  # Field name made lowercase.
    pago = models.IntegerField()
    valor = models.IntegerField()
    datapagamento = models.DateField(db_column='dataPagamento', blank=True, null=True)  # Field name made lowercase.
    dataemissao = models.DateField(db_column='dataEmissao', blank=True, null=True)  # Field name made lowercase.
    valordescontado = models.IntegerField(db_column='valorDescontado', blank=True, null=True)  # Field name made lowercase.
    valorpago = models.IntegerField(db_column='valorPago', blank=True, null=True)  # Field name made lowercase.
    datacompensacao = models.DateField(db_column='dataCompensacao', blank=True, null=True)  # Field name made lowercase.
    valorfumcad = models.IntegerField(db_column='valorFUMCAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Boleto'


class Cidade(models.Model):
    nome = models.CharField(max_length=40)
    idconv = models.CharField(db_column='idConv', max_length=10)  # Field name made lowercase.
    convenio = models.CharField(max_length=10)
    patrocinador1 = models.CharField(max_length=150)
    patrocinadorlink1 = models.CharField(db_column='patrocinadorLink1', max_length=150)  # Field name made lowercase.
    patrocinador2 = models.CharField(max_length=150)
    patrocinadorlink2 = models.CharField(db_column='patrocinadorLink2', max_length=150)  # Field name made lowercase.
    patrocinador3 = models.CharField(max_length=150)
    patrocinadorlink3 = models.CharField(db_column='patrocinadorLink3', max_length=150)  # Field name made lowercase.
    patrocinador4 = models.CharField(max_length=150)
    patrocinadorlink4 = models.CharField(db_column='patrocinadorLink4', max_length=150)  # Field name made lowercase.
    patrocinador5 = models.CharField(max_length=150)
    patrocinadorlink5 = models.CharField(db_column='patrocinadorLink5', max_length=150)  # Field name made lowercase.
    patrocinador6 = models.CharField(max_length=150)
    patrocinadorlink6 = models.CharField(db_column='patrocinadorLink6', max_length=150)  # Field name made lowercase.
    banner = models.CharField(max_length=255, blank=True, null=True)
    porcentagemfundo = models.IntegerField(db_column='porcentagemFundo')  # Field name made lowercase.
    possuiprojetos = models.IntegerField(db_column='possuiProjetos')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Cidade'


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
    porquedoar = models.CharField(db_column='porqueDoar', max_length=5000, blank=True, null=True)  # Field name made lowercase.
    sigla = models.CharField(max_length=50)
    site = models.CharField(max_length=100, blank=True, null=True)
    facebook = models.CharField(max_length=100, blank=True, null=True)
    permissoes = models.IntegerField()
    ativo = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    idcidade = models.IntegerField(db_column='idCidade')  # Field name made lowercase.
    projetodatainicio = models.DateField(db_column='projetoDataInicio', blank=True, null=True)  # Field name made lowercase.
    projetodataencerramento = models.DateField(db_column='projetoDataEncerramento', blank=True, null=True)  # Field name made lowercase.
    projetometaarrecadacao = models.IntegerField(db_column='projetoMetaArrecadacao', blank=True, null=True)  # Field name made lowercase.
    login = models.CharField(primary_key=True, max_length=20)

    class Meta:
        managed = False
        db_table = 'Instituicao'


class Pessoa(models.Model):
    documento = models.CharField(primary_key=True, max_length=14)
    senha = models.CharField(max_length=64)
    tipodocumento = models.IntegerField(db_column='tipoDocumento')  # Field name made lowercase.
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
        managed = False
        db_table = 'Pessoa'
