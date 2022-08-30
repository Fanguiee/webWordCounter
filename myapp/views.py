from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    context = {
        'name' : 'Ives',
        'adress' : 'London'
    }
    return render(request, 'index.html', context)

def counter(request):
    words = request.POST['words'] #NOTES: get that in the reqeust, which is named 'words'
    numOfWords = len(words.split())
    return render(request, 'counter.html', {"numOfWords" : numOfWords})

