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
from django.contrib import messages


class ManageNotes(LoginRequiredMixin, ListView): 
    template_name = "main/notes/manage_notes.html"
    model = Notes

    def get_queryset(self): 

        # Get Categories From Users First

        # Check if Filter Is Present
        if self.request.GET.get("filter"):
            filter_id = self.request.GET.get("filter")
            categories_queryset = Categories.objects.filter(id=filter_id).order_by('name')
        else: 
            categories_queryset = Categories.objects.filter(user=self.request.user).order_by('name')

        categories = []

        for category in categories_queryset:
            categories.append({"id": category.id, "name": category.name, "notes": ""}) 

        # Put Notes From Categories in List
        for category in categories: 
            notes = Notes.objects.filter(category=category["id"]).order_by('id')
            category.update({"notes": list(notes)})

        return categories

    def get_context_data(self, **kwargs):    

        context = super().get_context_data(**kwargs)

        if self.request.GET.get("filter"):
            filter_id = self.request.GET.get("filter")

            # Checking for No Notes or Categories 
            categories = Categories.objects.filter(user=self.request.user)
            category_filtered = Categories.objects.get(id=filter_id)
            notes_count = Notes.objects.filter(category=category_filtered).count() 

            context["filter_id"] = filter_id
            context["filter_name"] = category_filtered.name

            context["categories"] = categories
            context["categories_count"] = categories.count()
            context["notes_count"] = notes_count

        else: 

            # Checking for No Notes or Categories 
            categories = Categories.objects.filter(user=self.request.user)
            notes_count = Notes.objects.filter(author=self.request.user).count()

            context["categories"] = categories
            context["categories_count"] = categories.count()
            context["notes_count"] = notes_count


        return context


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
            messages.add_message(request, messages.SUCCESS, "New Note Added")  
            return redirect('main:Notes')
        else: 
            return render(request, "main/notes/new_note.html", context)


class UpdateNote(LoginRequiredMixin, UpdateView): 
    template_name = "main/notes/update_note.html"
    form_class = NotesForm 

    def get_object(self): 
        id_ = self.kwargs.get("id") 
        return get_object_or_404(Notes, id=id_)

    def get_success_url(self):
        messages.add_message(self.request, messages.INFO, "Note Updated")  
        return reverse("main:Notes")
    

class DeleteNote(LoginRequiredMixin, DeleteView): 
    template_name = "main/notes/delete_note.html"

    def get_object(self): 
        id_ = self.kwargs.get("id")
        return get_object_or_404(Notes, id=id_)

    def get_success_url(self):
        messages.add_message(self.request, messages.WARNING, "Note Deleted")  
        return reverse("main:Notes") 