from django.shortcuts import render

def index(request):
    return render(request, 'spac3logs/index.html')