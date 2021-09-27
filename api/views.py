from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .models import Company
from django.http.response import JsonResponse
import json
# from django.shortcuts import render # para renderisar plantillas
# Create your views here.
# Creamos vista basada en una clase

class CompanyView(View):

    @method_decorator(csrf_exempt) # para que nos exonere la resticcion csrf
    def dispatch(self, request, *args, **kwargs): #funcion que se ejecuta al hacer una peticion
        return super().dispatch(request, *args, **kwargs)

    def get(self,request,id=0):
        if(id>0):
            companies = list(Company.objects.filter(id=id).values()) #por el ORM hacemos un select de todas las companias que tengan un mismo id con sus valores y lo guardamos en una lista (arreglo) de python
            if len(companies)>0: 
                company=companies[0] #guardamos la compania en una variable
                datos={'message':"Success",'companies':company}
            else:
                datos={'message':"compania no encontrada..."}
            return JsonResponse(datos)
        else:
            companies = list(Company.objects.values()) #por el ORM hacemos un select de todas las companias y lo guardamos en una lista (arreglo) de python
            if len(companies)>0: #si el tamano del archivo es > 0
                datos={'message':"Success",'companies':companies}
            else:
                datos={'message':"companias no encontradas..."}
            return JsonResponse(datos)

    def post(self,request):
        #print(request.body)
        jd = json.loads(request.body)
        #print(jd)
        Company.objects.create(name=jd['name'],website=jd['website'],foundation=jd['foundation'])
        datos = {'message':"Success"}
        return JsonResponse(datos)

    def put(self,request,id):
        jd = json.loads(request.body)
        companies = list(Company.objects.filter(id=id).values()) #por el ORM hacemos un select de todas las companias que tengan un mismo id con sus valores y lo guardamos en una lista (arreglo) de python
        if len(companies)>0:
            company = Company.objects.get(id=id) 
            company.name=jd['name']
            company.website=jd['website']
            company.foundation=jd['foundation']
            company.save() #guardar los cambios
            datos = {'message':"Success"}
        else:
            datos={'message':"Esta compania no existe"}
        return JsonResponse(datos)
    
    def delete(self,request,id):
        companies = list(Company.objects.filter(id=id).values()) #por el ORM hacemos un select de todas las companias que tengan un mismo id con sus valores y lo guardamos en una lista (arreglo) de python
        if len(companies)>0:
            Company.objects.filter(id=id).delete() #obtenemos la compania y la eliminamos
            datos = {'message':"Success"}
        else:
            datos={'message':"Esta compania no existe"}
        return JsonResponse(datos)

