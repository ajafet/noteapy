from main.models import Notes, Categories, Favorites
from django.views import View
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse 
from django.contrib import auth
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from main.forms import NotesForm
from django.http import HttpResponse
from django.db.models import Q
from django.http import Http404

## TO-DO ## 
# View Liked Notes
# Remove Liked Notes  
# Search Liked Notes 
# Pagination on Liked Notes

@login_required
def make_my_favorite(request):
    if request.method == "GET":

        note_id = request.GET.get('note_id')
        user = request.user 

        # Get Note Object 
        note = Notes.objects.get(id=note_id)

        # Increase Note's Number of Favorites By One 
        note.num_of_favorites = note.num_of_favorites + 1 
        note.save() 

        # Create Favorite Row In Favorites Table
        favorite = Favorites(user=user, note=note)
        favorite.save() 

        return HttpResponse("SUCCESS")

    else:
        raise Http404  


@login_required
def remove_favorite(request):
    if request.method == "GET":

        note_id = request.GET.get('note_id')
        user = request.user 

        # Get Note Object 
        note = Notes.objects.get(id=note_id)

        # Decrease Note's Number of Favorites By One 
        note.num_of_favorites = note.num_of_favorites - 1 
        note.save() 

        # Delete Favorites Row in Favorites Table
        favorite = Favorites.objects.get(user=user, note=note)
        favorite.delete()

        return HttpResponse("SUCCESS")

    else:
        raise Http404  



