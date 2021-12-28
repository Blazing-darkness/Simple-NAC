from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.radius, name='home'),
    path('NasAnlegen.html', views.NasAnlegen, name='Seite_01'),
    path('NasAnzeigen.html', views.NasAnzeigen, name='Seite_02'),
    path('RadacctAnlegen.html', views.RadacctAnlegen, name='Seite_03'),
    path('RadacctAnzeigen.html', views.RadacctAnzeigen, name='Seite_04'),
    path('RadcheckAnlegen.html', views.RadcheckAnlegen, name='Seite_05'),
    path('RadcheckAnzeigen.html', views.RadcheckAnzeigen, name='Seite_06'),
    path('RadgroupcheckAnlegen.html', views.RadgroupcheckAnlegen, name='Seite_07'),
    path('RadgroupcheckAnzeigen.html', views.RadgroupcheckAnzeigen, name='Seite_08'),
    path('RadgroupreplyAnlegen.html', views.RadgroupreplyAnlegen, name='Seite_09'),
    path('RadgroupreplyAnzeigen.html', views.RadgroupreplyAnzeigen, name='Seite_10'),
    path('RadpostauthAnlegen.html', views.RadpostauthAnlegen, name='Seite_11'),
    path('RadpostauthAnzeigen.html', views.RadpostauthAnzeigen, name='Seite_12'),
    path('RadreplyAnlegen.html', views.RadreplyAnlegen, name='Seite_13'),
    path('RadreplyAnzeigen.html', views.RadreplyAnzeigen, name='Seite_14'),
    path('RadusergroupAnlegen.html', views.RadusergroupAnlegen, name='Seite_15'),
    path('RadusergroupAnzeigen.html', views.RadusergroupAnzeigen, name='Seite_16'),
    path('CoA.html', views.CoA, name='Seite_17'),
    path('Apply.html', views.Apply, name='Seite_18')
]
