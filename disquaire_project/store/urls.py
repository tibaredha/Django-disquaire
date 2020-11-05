from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
	path('tiba/', views.tiba, name='tiba'),
	path('redha/', views.redha, name='redha'),
	path('mimi/', views.mimi, name='mimi'),
	
]