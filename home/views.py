from django.shortcuts import render

# Create your views here.


def homeView(request):
    tepmplate = 'home/home.html'
    context = {}
    return render(request, tepmplate, context)
