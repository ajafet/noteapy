from main.models import Notes, Favorites
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


class SearchNotes(LoginRequiredMixin, ListView): 
    template_name = "main/search/search_notes.html"
    paginate_by = 10
    model = Notes

    def get_queryset(self, **kwargs):

        # Get Search Text
        search_text = self.request.GET.get('search_text')

        if search_text: 
            object_list = self.model.objects.filter(Q(title__contains=search_text) | Q(content__contains=search_text)).order_by('id')

            object_list = list(object_list)

            # Check if Note is Liked or Disliked 
            for note in object_list: 
                
                is_favorite = Favorites.objects.filter(Q(user=self.request.user) & Q(note=note)).count()
                
                if is_favorite == 1: 
                    note.is_favorite = True
                else: 
                    note.is_favorite = False


        else: 
            object_list = []

        return object_list


    def get_context_data(self, **kwargs):    

        # Making URL Variable Available In Template

        search_text = self.request.GET.get('search_text')
        
        context = super().get_context_data(**kwargs)
        context["search_text"] = search_text        

        return context
