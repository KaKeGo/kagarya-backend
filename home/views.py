from django.shortcuts import render

from .models import ShowApiUrl

# Create your views here.


def homeView(request):
    links = ShowApiUrl.objects.all()
    tepmplate = 'home/home.html'
    context = {
        'links': links
    }
    return render(request, tepmplate, context)
