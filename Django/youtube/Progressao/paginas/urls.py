from django.urls import path
from .views import PaginaInicial

urlpatterns = [
    path('', PaginaInicial.as_view(), name='inicio'),
    # path('endereço/', MinhaView.as_view(), name='nome-da-url'),
]