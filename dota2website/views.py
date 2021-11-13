from django.shortcuts import render

def index(request):
    """The home page for dota2website"""
    return render(request, 'dota2website/index.html')
