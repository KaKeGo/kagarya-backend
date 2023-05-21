from django.shortcuts import render

from .models import CategoryApi

# Create your views here.


def homeView(request):
    categorys = CategoryApi.objects.all()
    tepmplate = 'home/home.html'
    context = {
        'categorys': categorys
    }
    return render(request, tepmplate, context)
