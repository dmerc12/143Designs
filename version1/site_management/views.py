from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Testimonial
from .forms import ContactForm

def home(request):
    testimonials = Testimonial.objects.filter(featured=True)
    context = {'testimonials': testimonials}
    return render(request, 'home.html', context)

def contact(request):
    try:
        form = ContactForm()
        if request.method == 'POST':
            form = ContactForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Your message has been successfully sent. We will be in contact soon! In the meantime, check out what's in stock in our store blow!")
                return redirect('store-home')
        context = {'form': form}
        return render(request, 'contact.html', context)
    except Exception as error:
        messages.error(request, str(error))
    