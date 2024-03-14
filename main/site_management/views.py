from django.shortcuts import render

# View for home page
def home(request):
    return render(request, 'home.html')

# View for admin home page
def admin_home(request):
    return render(request, 'admin_home.html')
