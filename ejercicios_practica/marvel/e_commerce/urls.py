from django.urls import path
from e_commerce.api.marvel_api_views import *

# Importamos las API_VIEWS:
from e_commerce.views import *


urlpatterns = [
    # NOTE: e_commerce base:
    path('base', PruebaView.as_view(), name ='base'),
    
    #TODO: Tarea! 
    path('cart' , CartView.as_view(), name = 'cart'),
    path('login', LoginView.as_view(), name='login'),
    path('thanks',ThanksView.as_view(), name = 'thanks'),
    path('user' , UserView.as_view(),name = 'user') ,
    path('wish', WishView.as_view(), name = 'wish'),
    ] 