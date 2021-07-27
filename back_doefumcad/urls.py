"""back_doefumcad URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from back_doefumcad import settings
from doafumcadmodel.api.views import BoletoViewSet, CidadeViewSet, PatrocinadorViewSet, PessoaViewSet, InstituicaoViewSet

router = routers.DefaultRouter()

router.register(r'boletos', BoletoViewSet, basename='Boleto')
router.register(r'cidades', CidadeViewSet, basename='Cidade')
router.register(r'pessoas', PessoaViewSet, basename='Pessoa')
router.register(r'patrocinadores', PatrocinadorViewSet, basename='Patrocinador')
router.register(r'instituicoes', InstituicaoViewSet, basename='Instituicao')


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework_social_oauth2.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
