from django.shortcuts import render

# written by Gowtham
# Create your views here.
def home_view(request):
    return render(request, 'testapp/home.html')


def movie_view(request):
    return render(request, 'testapp/movie.html')


def politics_view(request):
    return render(request, 'testapp/politics.html')


def sports_view(request):
    return render(request, 'testapp/sports.html')
