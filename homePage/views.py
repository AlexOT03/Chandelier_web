from django.shortcuts import render
from django.views import View
from ubicaciones.models import Location
from estados.models import State
from tematicas.models import Theme

# Create your views here.
class indexHome(View):
    def get(self, request, *args, **kwargs):
        locations = Location.objects.all()
        estados = State.objects.all()
        temas = Theme.objects.all()
        return render(request, 'index.html', {'locations': locations, 'estados': estados, 'temas': temas})
    
class fastQuoteHome(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'fastQuote.html')
    
class quoteHome(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'quote.html')
    
class locationHome(View):
    # def get(self, request, reference ,id):
    #     temas = Theme.objects.all()
    #     tema = Theme.objects.get(id=id)
    #     estado = State.objects.get(id=id)
    #     new_reference = reference
    #     return render(request, 'location.html', {
    #         'temas':temas,
    #         'tema':tema,
    #         'estado':estado,
    #         'new_reference':new_reference,
    #     })
    def get(self, request ,reference, id):
        temas = Theme.objects.all()
        new_reference = reference
        places = Location.objects.filter(theme_id=id)
        return render(request, 'location.html',{
            'temas':temas,
            'places':places,
            'new_reference':new_reference,
        })

class locationInfoHome(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'locationInfo.html')
    
class aboutUsHome(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'aboutUs.html')
    
class contactHome(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'contactUs.html')