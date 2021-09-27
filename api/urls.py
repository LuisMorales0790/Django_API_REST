from django.urls import path #para establecer rutas
from .views import CompanyView

urlpatterns=[   #lista o arreglo
    path('companies/', CompanyView.as_view(), name='companies_list'), # ruta para traer todas las companias
    path('companies/<int:id>', CompanyView.as_view(), name='companies_process') # ruta para traer una compania por el id
]