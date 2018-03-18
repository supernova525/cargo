from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, ListView
from django.urls import reverse
from core.models import Delivery, Prealert
from core.forms import PrealertForm

class LandingView(TemplateView):
    template_name="frontend/landing.html"

class DashBoardView(ListView):
    template_name="frontend/dashboard.html"
    model = Delivery


    def get_queryset(self, **kwargs):
        return super(DashBoardView, self).get_queryset(**kwargs).filter()


class PrealertView(ListView):
    template_name = "frontend/prealerts.html"
    model = Prealert

    def get_queryset(self):
        return super(PrealertView, self).get_queryset().filter()

    def get_context_data(self):
        context = super(PrealertView, self).get_context_data()
        context['form'] = PrealertForm()
        return context

    def post(self, request):
        form = PrealertForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('prealerts'))
def ContactPage(request):
    return render(request, 'frontend/contactPage.html')




    
