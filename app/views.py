from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import FormView
from app.forms import *
# Create your views here.
class CDV_FORMS(FormView):
    template_name='CDV_FORMS.html'
    form_class=SchoolForm
    def form_valid(self, form) :
        form.save()
        return HttpResponse('data is saved....')