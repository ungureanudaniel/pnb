from django.shortcuts import render

def home(request):
    template = 'services/index.html'
    return render(request, template, {})
