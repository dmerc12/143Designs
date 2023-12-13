from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def home(request):
    return render(request, 'other/home.html')

def register(request):
    form = UserCreationForm()
    return render(request, 'main/register.html', {'form': form})
