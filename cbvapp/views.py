from django.shortcuts import render
from django.views.generic import View, ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import Employee


# Create your views here.


class classbasedview(View):
    def get(self, request):
        return HttpResponse('<p> Class Based View Example')

# Template based class view
class Templatebasedclassview(TemplateView):
    template_name = 'cbvapp/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'templatesample'
        context['age'] = 25
        return context

# List View  need a model here definitely
class Listbasedview(ListView):
    model = Employee   # no need to mention template file here , django will search for Modelname_list.html
    # default template name is Employee_list.html
    # default context_object_name is employee_list

class Detailbaseview(DetailView):
    model = Employee
    # default template name is Employee_detail.html
    # default context_object_name is employee or object


class Employeecreateview(CreateView):
    model = Employee
    #fields = ('EmpID', 'Empname', 'EmpAge', 'EmpSal', 'EmpDesignation', 'Empcity')
    fields = '__all__'
    # template it will search for modelname_form.html (Employee_form.html)


class Employeeupdateview(UpdateView):
    model = Employee
    fields = ('Empname', 'EmpAge', 'EmpSal', 'EmpDesignation', 'Empcity')

class Employeedeleteview(DeleteView):
    model = Employee
    success_url = reverse_lazy('list')
