from django.shortcuts import render
from django.http import HttpResponse, Http404
# Create your views here.
def about(request):
    return render(request, 'about.html', locals())