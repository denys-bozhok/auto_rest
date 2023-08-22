from django.urls import path

from . import views


urlpatterns = [
    path('autos', views.autos),
    path('auto/<int:arg>', views.auto),
    path('owners', views.owners),
    path('owner/<int:arg>', views.owner),
    path('auto_passports', views.auto_passports),
    path('auto_passport/<int:arg>', views.auto_passport),
    
]
