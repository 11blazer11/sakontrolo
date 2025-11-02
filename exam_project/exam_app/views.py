from django.shortcuts import render

def home_view(request):
    return render(request, 'home.html')

def films_view(request):
    films = {
        "Joker": 7.5,
        "Inception": 8.8,
        "ragaca": 8
    }

    context = {
        "title": "Films",
        "films": films,
    }
    return render(request, 'film.html', context)