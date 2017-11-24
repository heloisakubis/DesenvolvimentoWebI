# -*- coding: utf-8 -*-
"""desenvWebI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""

from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.core.urlresolvers import reverse_lazy
from appWeb.views import *
from django.contrib.auth.views import login, logout
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', login_required(logout), {'next_page': reverse_lazy('index')}, name='logout'),
    url(r'^$', IndexListView.as_view(), name='index'),

    # ----------------- CADASTROS -----------------
    url(r'^aluno/search$', AlunoOcorrenciaListView.as_view(), name='filtra_aluno'),
    url(r'^ocorrencia/add$', OcorrenciaCreateView.as_view(), name='cadastra_ocorrencia'),
    url(r'^ocorrencia/add/(?P<pk>\d+)/$', OcorrenciaCreateView.as_view(), name='cadastra_aluno_ocorrencia'),
    url(r'^tipo_permissao/add$', TipoOcorrenciaCreateView.as_view(), name='cadastra_tipo_ocorrencia'),
    url(r'^tipo_oferta/add$', TipoOfertaCreateView.as_view(), name='cadastra_tipo_oferta'),
    url(r'^tipo_func/add$', TipoFuncionarioCreateView.as_view(), name='cadastro_tipo_funcinario'),
    url(r'^aluno/add$', AlunoCreateView.as_view(), name='cadastra_aluno'),
    url(r'^funcionario/add$', FuncionarioCreateView.as_view(), name='cadastra_funcionario'),
    url(r'^turma/add$', TurmaCreateView.as_view(), name='cadastra_turma'),
    url(r'^curso/add$', CursoCreateView.as_view(), name='cadastra_curso'),

    # ----------------- EDIÇÃO -----------------
    url(r'^permissao/edit/(?P<pk>\d+)/$', OcorrenciaUpdateView.as_view(), name='edita_ocorrencia'),
    url(r'^aluno/edit/(?P<pk>\d+)/$', AlunoUpdateView.as_view(), name='edita_aluno'),
    url(r'^funcionario/edit/(?P<pk>\d+)/$', FuncionarioUpdateView.as_view(), name='edita_funcionario'),
    url(r'^turma/edit/(?P<pk>\d+)/$', TurmaUpdateView.as_view(), name='edita_turma'),
    url(r'^curso/edit/(?P<pk>\d+)/$', CursoUpdateView.as_view(), name='edita_curso'),

    # ----------------- REMOÇÃO -----------------
    url(r'^aluno/delete/(?P<pk>\d+)/$', AlunoDeleteView.as_view(), name='exclui_aluno'),
    url(r'^funcionario/delete/(?P<pk>\d+)/$', FuncionarioDeleteView.as_view(), name='exclui_funcionario'),
    url(r'^turma/delete/(?P<pk>\d+)/$', TurmaDeleteView.as_view(), name='exclui_turma'),
    url(r'^curso/delete/(?P<pk>\d+)/$', CursoDeleteView.as_view(), name='exclui_curso'),

    # ----------------- LISTAGEM -----------------
    url(r'^lista/funcionario/$', FuncionarioListView.as_view(), name='funcionario_list'),
    url(r'^lista/turma/$', TurmaListView.as_view(), name='turma_list'),
    url(r'^lista/curso/$', CursoListView.as_view(), name='curso_list'),
    url(r'^lista/aluno/$', AlunoListView.as_view(), name='aluno_list'),
    url(r'^lista/permissao/$', OcorrenciaListView.as_view(), name='ocorrencia_list'),


]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)