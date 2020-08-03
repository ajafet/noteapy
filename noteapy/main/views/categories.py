from main.models import Categories, Notes
from django.views import View
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse 
from django.contrib import auth
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from main.forms import CategoryForm
from django.http import HttpResponse
from django.db.models import Q


class ManageCategories(LoginRequiredMixin, ListView): 
    template_name = "main/categories/manage_categories.html"
    paginate_by = 10
    model = Categories

    def get_queryset(self):

        search_text = self.request.GET.get('search_text')

        if search_text and search_text != "":
            object_list = self.model.objects.filter(Q(name__contains=search_text)).order_by('id')
        else:
            object_list = self.model.objects.all().order_by('id') 

        categories = []

        for obj in object_list: 
            notes_count = Notes.objects.filter(category=obj).count()
            categories.append({"categories": obj, "notes_count": notes_count})

        return categories


class NewCategory(LoginRequiredMixin, View): 

    def get(self, request): 
        form = CategoryForm()
        context = {
            "form": form,
        }
        return render(request, "main/categories/new_category.html", context)

    def post(self, request): 
        form = CategoryForm(request.POST) 
        context = {
            "form": form,
        }
        if form.is_valid():
            form_instance = form.save(commit=False)
            form_instance.user = request.user
            form_instance.save()
            return redirect('main:Categories')
        else: 
            return render(request, "main/categories/new_category.html", context)


class ViewCategory(LoginRequiredMixin, DetailView): 
    template_name = "main/categories/view_category.html"

    def get_object(self): 
        id_ = self.kwargs.get("id")
        return get_object_or_404(Categories, id=id_)

    def get_context_data(self, **kwargs):    

        category = self.get_object()
        notes_in_category = Notes.objects.filter(category=category)
        childs_list = list(notes_in_category)

        context = super().get_context_data(**kwargs)                     
        context["notes"] = notes_in_category
        context["category_id"] = category.id

        return context


class UpdateCategory(LoginRequiredMixin, UpdateView): 
    template_name = "main/categories/update_category.html"
    form_class = CategoryForm 

    def get_object(self): 
        id_ = self.kwargs.get("id") 
        return get_object_or_404(Categories, id=id_)

    def get_context_data(self, **kwargs):          
        context = super().get_context_data(**kwargs)                     
        context["category_id"] = self.kwargs.get("id")
        return context

    def get_success_url(self):
        id_ = self.kwargs.get("id")
        return reverse("main:View_Category", kwargs={"id": id_})


class DeleteCategory(LoginRequiredMixin, DeleteView): 
    template_name = "main/categories/delete_category.html"

    def get_object(self): 
        id_ = self.kwargs.get("id")
        return get_object_or_404(Categories, id=id_)

    def get_context_data(self, **kwargs):    

        category = self.get_object()
        notes_in_category = Notes.objects.filter(category=category)
        childs_list = list(notes_in_category)

        context = super().get_context_data(**kwargs)                     
        context["notes"] = notes_in_category
        context["category_id"] = category.id

        return context

    def get_success_url(self):
        return reverse("main:Categories") 

    