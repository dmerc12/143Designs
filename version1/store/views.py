from site_management.models import Testimonial
from django.shortcuts import render

def home(request):
    testimonials = Testimonial.objects.filter(featured=True)
    context = {'testimonials': testimonials}
    return render(request, 'home.html', context)

def contact(request):
    return render(request, 'contact.html')
