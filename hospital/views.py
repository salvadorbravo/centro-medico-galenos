from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request, 'hospital/index.html')

def adminclick_view(request):
    return render(request,'hospital/adminclick.html')

def doctorclick_view(request):
    return render(request,'hospital/doctorclick.html')

def patientclick_view(request):
    return render(request,'hospital/patientclick.html')