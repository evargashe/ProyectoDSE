from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *
# Create your views here.
class HomeView(TemplateView):
    template_name="home.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['myname'] = "Edwar Vargas"
        context['product_list']= Product.objects.all()
        context['allcategories']= Category.objects.all()
        return context


class AboutView(TemplateView):
    template_name="about.html"

class ContactView(TemplateView):
    template_name = "contactus.html"


class AllProductsView(TemplateView):
    template_name = "allproducts.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['allcategories'] = Category.objects.all()
        return context


