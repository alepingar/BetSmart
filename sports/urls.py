from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_eventos, name='lista_eventos'),
    path('apuesta/<int:evento_id>/', views.hacer_apuesta, name='hacer_apuesta'),
]
