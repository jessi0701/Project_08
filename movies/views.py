from django.shortcuts import render,redirect
from .models import Movie,Genre,Score
from .forms import MovieForm
# Create your views here.
def list(request):
    movies = Movie.objects.all()
    return render(request, 'movies/list.html',{'movies':movies})

def new(request):
    
    if request.method=='POST':
        movie_form = MovieForm(request.POST)
        if movie_form.is_valid():
            movie = movie_form.save()
            
            return redirect("movies:detail",movie.id)
        
    else:        
        form = MovieForm()
    return render(request, 'movies/form.html',{'form':form})
    
def detail(request,id):
    movie = Movie.objects.get(id=id)
    return render(request, 'movies/detail.html',{'movie':movie})
    
def update(request,id):
    movie = Movie.objects.get(id=id)
    
    if request.method=='POST':
        movie_form = MovieForm(request.POST, instance=movie)
        if movie_form.is_valid():
            movie = movie_form.save()
            return redirect("movies:detail", movie.id)
            
    else:
        movie_form = MovieForm(instance=movie)
    return render(request, 'movies/form.html',{'form':movie_form})
    
        