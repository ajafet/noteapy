from main.models import Notes
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

        # Get Search Text and Option 
        search_text = self.request.GET.get('search_text')
        search_option = self.request.GET.get('search_option')

        if search_option == 1: 

            # Get Notes 
            object_list = self.model.objects.filter(Q(title__contains=search_text) | Q(content__contains=search_text)).order_by('id')

        elif search_option == 2: 

            # Get Categories 
            object_list = Categories.objects.filter(Q(name__contains=search_text)).order_by('id')

            categories = []

            for obj in object_list: 
                notes_count = Notes.objects.filter(category=obj).count()
                categories.append({"categories": obj, "notes_count": notes_count})

            object_list = categories 

        else: 

            # Get Nothing 
            object_list = [] 


        return object_list


    def get_context_data(self, **kwargs):    

        # Get Request Data
        search_text = self.request.GET.get('search_text')
        search_option = self.request.GET.get('search_option')
        
        context = super().get_context_data(**kwargs)

        # Getting Search Option From URL and Passing Through Context 
        if search_option == 1:             
            context["search_option"] = 1
        elif search_option == 2: 
            context["search_option"] = 2
        
        # Determine If First Time Loading Page or Nothing Found
        if len(search_text) == 0: 
            context["nothing_found"] = 1 
        else: 
            context["nothing_found"] = 0 

        return context
