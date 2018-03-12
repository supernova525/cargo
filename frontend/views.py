from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from core.models import Delivery

class LandingView(TemplateView):
    template_name="frontend/landing.html"

class DashBoardView(ListView):
    template_name="frontend/dashboard.html"
    model = Delivery


    def get_queryset(self, **kwargs):
        return super(DashBoardView, self).get_queryset(**kwargs).filter()
        


    
