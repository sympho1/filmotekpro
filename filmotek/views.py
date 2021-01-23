from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Realisator, Film
from .forms import RealisatorForm, FilmForm
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'filmotek/home.html')


def all_films(request):
    films = Film.objects.all().order_by('title')

    return render(request, "filmotek/list_films.html", {"all_films": films})

def get_film(request, film_id):
    film = get_object_or_404(Film, pk=film_id)
    return render(request, 'filmotek/get_film.html', context={'film': film})
    pass

def add_film(request):
    if request.method == "POST":
        form = FilmForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            release_date = form.cleaned_data["release_date"]
            # vote = form.cleaned_data["vote"]
            # score = form.cleaned_data["score"]
            realisator = form.cleaned_data["realisator"]

            film = Film(title=title, release_date=release_date, realisator=realisator)
            film.save()
            # messages.success(request, "Film ajouté avec succès")
            return redirect(reverse('all-films'))
        else:
            form = FilmForm()
            
            return render(request, 'filmotek/add_film.html', {"form": form})
            
    else:
        form = FilmForm()
        # messages.error(request, "Champs invalides")
        return render(request, 'filmotek/add_film.html', {"form": form})

def delete_film(request, film_id):
    film = get_object_or_404(Film, pk=film_id)
    ctx = {'film_name': film.title}

    if request.method == "POST":
        film.delete()
        return redirect(reverse('all-films'))
    return render(request, 'filmotek/delete_film.html', ctx)

def realisators(request):
    realisators = Realisator.objects.all()
    ctx = {
        "all_realisators": realisators
    }

    return render(request, "filmotek/list_realisators.html", ctx)

def get_realisator(request, realisator_id):
    realisator = get_object_or_404(Realisator, pk=realisator_id)
    return render(request, 'filmotek/get_realisator.html', context={'realisator': realisator})

def delete_realisator(request, id):
    realisator = get_object_or_404(Realisator, pk=id)
    ctx = {'realisator': realisator}

    if request.method == "POST":
        realisator.delete()
        return redirect(reverse('all-realisators'))
    return render(request, 'filmotek/delete_realisator.html', ctx)

def get_realisator_films(request, realisator_id):
    realisator = get_object_or_404(Realisator, pk=realisator_id)
    realisator_films = realisator.film_set.all()
    ctx = {"realisator_films": realisator_films, "realisator": realisator}
    return render(request, 'filmotek/realisator_films.html', ctx)
    pass

def add_realisator(request):
    if request.method == "POST":
        realisator_form = RealisatorForm(request.POST)
        if realisator_form.is_valid():
            name = realisator_form.cleaned_data["name"]
            realisator = Realisator(name=name)
            realisator.save()
            return redirect(reverse('all-realisators'))
    else:
        realisator_form = RealisatorForm()
        return render(request, 'filmotek/add_realisator.html', {"form": realisator_form})

    # return render(request, 'filmotek/add_realisator.html')
    pass

