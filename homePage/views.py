from django.shortcuts import render
from django.views import View

# Create your views here.
class indexHome(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')
    
class quoteHome(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'fastQuote.html')
    
class locationHome(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'location.html')

class locationInfoHome(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'locationInfo.html')
    
class aboutUsHome(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'aboutUs.html')
    
class contactHome(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'contactUs.html')