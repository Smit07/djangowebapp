from django.shortcuts import render
from .models import Product


def home(request):

    products=Product.objects.all()
    return render(request, 'Home.html', {'products':products})

def your_view(request):
    # Assuming you have a variable named 'motorcycle_background_image' that contains the URL of the motorcycle background image
    motorcycle_background_image = '/Users/biswasmitlenka/website/ecom/static/assets/motorcycle-background.jpg'
    return render(request, 'Home.html', {'motorcycle_background_image': motorcycle_background_image})
