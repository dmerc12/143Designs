from django.shortcuts import render, redirect
from users.models import CustomUser, Customer
from django.contrib import messages
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
            customer = Customer.objects.create(first_name=form.cleaned_data['first_name'], last_name=form.cleaned_data['last_name'], email=form.cleaned_data['email'], phone_number=form.cleaned_data['phone_number'])
            Message.objects.create(customer=customer, title=form.cleaned_data['title'], message=form.cleaned_data['message'])
            messages.success(request, 'Your message has been successfully sent. We will be in contact soon!\nIn the meantime, check out our store!')
            return redirect('home')
    else:
        form = ContactForm()
    return render(request, 'site_management/messages/contact.html', {'form': form})

# View for admin messages home page
def messages_home(request):
    if (request.user.is_superuser or CustomUser.objects.filter(user=request.user.id, role='admin').exists()) and request.user.is_authenticated:
        contacts = Message.objects.all()
        return render(request, 'site_management/messages/home.html', {'contacts': contacts})
    else:
        messages.error(request, 'You must be a site admin access this page!')
        return redirect('home')

# View for delete message page
def delete_message(request, message_id):
    if (request.user.is_superuser or CustomUser.objects.filter(user=request.user.id, role='admin').exists()) and request.user.is_authenticated:
        message = Message.objects.get(pk=message_id)
        if request.method == 'POST':
            message.delete()
            messages.success(request, f'The message has been deleted!')
            return redirect('messages-home')
        return render(request, 'site_management/messages/delete.html', {'message': message})
    else:
        messages.error(request, 'You must be a site admin access this page!')
        return redirect('home')
