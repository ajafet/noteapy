from main.models import Notes, Categories
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


class ManageNotes(LoginRequiredMixin, ListView): 
    template_name = "main/notes/manage_notes.html"
    model = Notes

    def get_queryset(self): 

        # Get Categories From Users First
        categories_queryset = Categories.objects.filter(user=self.request.user).order_by('name')
        categories = []

        for category in categories_queryset:
            categories.append({"id": category.id, "name": category.name, "notes": ""}) 

        # Put Notes From Categories in List
        for category in categories: 
            notes = Notes.objects.filter(category=category["id"]).order_by('id')
            category.update({"notes": list(notes)})

        return categories


class NewNote(LoginRequiredMixin, View): 

    def get(self, request): 
        form = NotesForm()
        context = {
            "form": form,
        }
        return render(request, "main/notes/new_note.html", context)

    def post(self, request): 
        form = NotesForm(request.POST) 
        context = {
            "form": form,
        }
        if form.is_valid():
            form_instance = form.save(commit=False)
            form_instance.author = request.user
            form_instance.num_of_favorites = 0
            form_instance.save()
            return redirect('main:Notes')
        else: 
            return render(request, "main/notes/new_note.html", context)
    