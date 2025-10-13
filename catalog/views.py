from django.shortcuts import render, get_object_or_404, redirect
from .forms import FilmForm, LookupForm
from .models import Film

def home(request):
    return render(request, 'index.html')

def create_film(request):
    if request.method == 'POST':
        form = FilmForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_films')
    else:
        form = FilmForm()
    films = Film.objects.order_by('MovieTitle')
    return render(request, 'add_video.html', {'form': form, 'videos': films})

def list_films(request):
    films = Film.objects.order_by('MovieTitle')
    return render(request, 'list_videos.html', {'videos': films})

def update_film(request, pk):
    film = get_object_or_404(Film, pk=pk)
    if request.method == 'POST':
        form = FilmForm(request.POST, instance=film)
        if form.is_valid():
            form.save()
            return redirect('list_films')
    else:
        form = FilmForm(instance=film)
    return render(request, 'add_video.html', {'form': form, 'videos': []})

def delete_film(request, pk):
    film = get_object_or_404(Film, pk=pk)
    if request.method == 'POST':
        film.delete()
        return redirect('list_films')
    return render(request, 'confirm_delete.html', {'video': film})

def lookup_film(request):
    found = None
    if request.method == 'POST':
        form = LookupForm(request.POST)
        if form.is_valid():
            MovieID = form.cleaned_data['MovieID']
            found = Film.objects.filter(MovieID=MovieID).first()
    else:
        form = LookupForm()
    return render(request, 'report_video.html', {'form': form, 'found': found})