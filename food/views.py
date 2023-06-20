from django.shortcuts import render
from .models import Category, Menu, Events, Testimonials, Gallery, Chefs
from .forms import ContactForm, ReservationForm

# Create your views here.

def IndexView(request):
    foods = Menu.objects.all()
    print(foods)
    categories = Category.objects.all()
    events = Events.objects.all()
    testimonials = Testimonials.objects.all()
    reservation = ReservationForm()
    gallery = Gallery.objects.all()
    chefs = Chefs.objects.all()

    context = {
        'foods': foods, 
        'categories': categories,
        'events': events,
        'testimonials': testimonials,
        'reservation': reservation,
        'gallery': gallery,
        'chefs': chefs,
        }
    return render(request, 'index.html',context=context)