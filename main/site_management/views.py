from django.shortcuts import render, redirect
from django.contrib import messages
from users.models import CustomUser
from .forms import ContactForm
from .models import Message

# View for home page
def home(request):
    return render(request, 'home.html')

# View for admin home page
def admin_home(request):
    if (request.user.is_superuser or CustomUser.objects.filter(user=request.user.id, role='admin').exists()) and request.user.is_authenticated:
        return render(request, 'admin_home.html')
    else:
        messages.error(request, 'You must be a site admin access this page!')
        return redirect('home')

# View for contact page
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been successfully sent. We will be in contact soon!\nIn the meantime, check out our store!')
            return redirect('home')
    else:
        form = ContactForm()
    return render(request, 'site_management/messages/contact.html', {'form': form})

# View for admin messages home
def messages_home(request):
    messages = Message.objects.all()
    return render(request, 'site_management/messages/home.html', {'messages': messages})
