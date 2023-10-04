from django.shortcuts import render

def index_view(request):
    return render(request, 'index.html')

def fleet_view(request):
    return render(request, 'fleet.html')

def about_view(request):
    return render(request, 'about.html')

def service_view(request):
    return render(request, 'service.html')
   
      
