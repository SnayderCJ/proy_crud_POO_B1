from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Doctor

# Create your views here.
def home(request):
   data={"title":"Medical","title1":"Sistema Medico Online"}
   #return HttpResponse("<h1>Pantalla de Inicio</h1>")
   #return JsonResponse(data)
   return render(request,'core/home.html',data)

def doctor_List(request):
    data={"title":"Medical","title1":"Consulta de Doctores"}
    doctores = Doctor.objects.all()
    data["doctores"]=doctores
    print(data)
    return render(request,"core/doctor/list.html",data)
 
def doctor_Create(request):
      data={"title":"Medical","title1":"Registro de Doctores"}
      
      return render(request,"core/doctor/create.html",data)