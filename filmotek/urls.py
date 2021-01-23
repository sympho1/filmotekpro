from django.urls import path 
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path("all-films", views.all_films, name="all-films"),
    path('film/<int:film_id>', views.get_film, name='film'),
    path('film/<int:film_id>/delete', views.delete_film, name='delete-film'),
    path('add-film', views.add_film, name='add-film'),
    path('all-realisators', views.realisators, name='all-realisators'),
    path('realisator/<int:realisator_id>', views.get_realisator, name="realisator"),
    path('realisator/<int:id>/delete', views.delete_realisator, name='delete-realisator'),
    path('realisator/<int:realisator_id>/films', views.get_realisator_films, name="realisator-films"),
    path('add-realisator', views.add_realisator, name='add-realisator'),
    path('realisator', views.get_realisator, name='realisator'),
]
