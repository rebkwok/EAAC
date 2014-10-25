
from django.shortcuts import render, HttpResponse, get_object_or_404


def home(request):

    return render(request, 'website/home.html', {'section': 'home'})

