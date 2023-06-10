from django.shortcuts import render, redirect
from django.views import View
from .models import Theme
from .form import ThemeForm

# Create your views here.
class ThemAdminView(View):
    def get(self, request, *args, **kwargs):
        form = ThemeForm(request.POST)
        temas = Theme.objects.all()
        return render(request, 'them.html', {'form': form, 'temas': temas, })

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = ThemeForm(request.POST, request.FILES)
            if form.is_valid():
                print('success')
                form.save()
            else:
                print('Invalid')
                form = ThemeForm()
        return redirect('themsAdmin')