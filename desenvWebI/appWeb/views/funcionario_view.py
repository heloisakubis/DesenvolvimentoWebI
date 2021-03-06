# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.generic import *
from appWeb.forms import FuncionarioForm
from appWeb.models.funcionario_model import FuncionarioModel


@method_decorator(login_required, name='dispatch')
class FuncionarioListView(ListView):
    queryset = FuncionarioModel.objects.filter(excluido=False).order_by('-id').distinct()
    paginate_by = 10


@method_decorator(login_required, name='dispatch')
class FuncionarioCreateView(CreateView):
    model = FuncionarioModel
    form_class = FuncionarioForm
    success_url = '/'


@method_decorator(login_required, name='dispatch')
class FuncionarioUpdateView(UpdateView):
    model = FuncionarioModel
    form_class = FuncionarioForm
    success_url = '/'


@method_decorator(login_required, name='dispatch')
class FuncionarioDeleteView(DeleteView):
    model = FuncionarioModel
    success_url = reverse_lazy('funcionario_list')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.excluido = True
        self.object.is_active = False
        self.object.save()
        success_url = self.get_success_url()
        return HttpResponseRedirect(success_url)

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)