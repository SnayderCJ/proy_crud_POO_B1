from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .models import Doctor
from .forms import DoctorForm

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
 
def doctor_create(request):
   data = {"title": "Doctores","title1": "Añadir Doctores"}
   if request.method == "POST":
      form = DoctorForm(request.POST)
      if form.is_valid():
         form.save()
         return redirect("core:doctor_list")
      else:
         data["form"] = form
         data["error"] = "Error al crear el Doctor."
         return render(request, "core/doctor/form.html", data)
   else:
      form = DoctorForm()
      data["form"] = form
   print(form)
   return render(request, "core/doctor/form.html", data)
            

