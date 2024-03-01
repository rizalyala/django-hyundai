from django.shortcuts import render, get_object_or_404
from .models import Vehicle

def home(request):
    vehicles = Vehicle.objects.all()
    return render(request,'main/main.html',{'vehicles': vehicles})

def about(request):
    return render(request,'main/about.html')

def contact(request):
    return render(request,'main/contact.html')

def vehicle_detail(request, id):
    vehicle = get_object_or_404(Vehicle, pk=id)
    return render(request, 'main/vehicle_detail.html', {'vehicle': vehicle})
