from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm

# View for home page
def home(request):
    return render(request, 'home.html')

# View for admin home page
def admin_home(request):
    return render(request, 'admin_home.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been successfully sent. We will be in contact soon!\nIn the meantime, check out our store!')
            return redirect('home')
    else:
        form = ContactForm()
    return render(request, 'site_management/contact.html', {'form': form})
