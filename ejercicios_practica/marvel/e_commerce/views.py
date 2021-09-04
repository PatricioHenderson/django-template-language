from django.shortcuts import render

# Importamos vistas genericas:
from django.views.generic import TemplateView

# Importamos los modelos que vamos a usar:
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User 
from e_commerce.models import *

class PruebaView(TemplateView):
    template_name = 'e-commerce/base.html'  

class CartView(TemplateView):
    template_name = 'e-commerce/cart.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['Cart'] = WishList.objects.filter(user_id=self.request.user.id, cart=True)
        
        return context

class LoginView(LoginView):
    template_name = 'e-commerce/login.html'

class ThanksView(TemplateView):
    template_name = 'e-commerce/thanks.html'

class UserView(TemplateView):
    template_name = 'e-commerce/user.html'    

class WishView(TemplateView):

    template_name = 'e-commerce/wish.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['WishList'] = WishList.objects.filter(user_id=self.request.user.id, favorite=True)
        
        return context
