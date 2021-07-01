from django.shortcuts import render
from .forms import CustomUserCreationForm

# Create your views here.

def registro(request):
    data = {
            'form': CustomUserCreationForm
            }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            return redirect(to='principal')
        data["form"] = formulario

    return render(request, 'registration/registro.html', data)