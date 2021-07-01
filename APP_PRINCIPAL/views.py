from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

# Create your views here.

def principal(request):
    return render(request, './principal.html')

@login_required
def acerca_de(request):
    return render(request, './acerca_de.html')

