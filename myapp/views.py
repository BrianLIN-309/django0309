from django.shortcuts import render
from django.http import HttpResponse, Http404
from myapp.models import Product
# Create your views here.
def about(request):
    html ='''<!DOCTYPE html>
        <html><head><title>About Myself</title></head>
        <body><h2>Min-Huang Ho</h2><hr>
        <p>hi i am 113245465</p>
        </body>
        </html>
        '''
def listing(request):
    products = Product.objects.all()
    return render(request, 'list.html', locals())