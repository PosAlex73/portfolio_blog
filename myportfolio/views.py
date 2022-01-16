from django.shortcuts import render
from django.views.generic import TemplateView


class General(TemplateView):
    template_name = 'general/general.html'
