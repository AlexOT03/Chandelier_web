from django.shortcuts import render, redirect
from django.views import View
from .models import State
from .form import StateForm

# Create your views here.
class StatesAdminView(View):
    def get(self, request, *args, **kwargs):
        form = StateForm(request.POST)
        estados = State.objects.all()
        return render(request, 'state.html', {'form': form, 'estados':estados, })

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = StateForm(request.POST, request.FILES)
            if form.is_valid():
                print('success')
                form.save()
            else:
                print('Invalid')
                form = StateForm()
        return redirect('statesAdmin')