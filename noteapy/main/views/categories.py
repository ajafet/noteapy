from main.models import Categories
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


class ManageCategories(LoginRequiredMixin, ListView): 
    template_name = "main/categories/manage_categories.html"
    paginate_by = 10
    model = Categories

    def get_queryset(self):

        search_text = self.request.GET.get('search_text')

        if search_text and search_text != "":
            object_list = self.model.objects.filter(user=self.request.user.id).order_by('id')
        else:
            object_list = self.model.objects.all().order_by('id') 

        return object_list

    # def get_context_data(self, **kwargs):          
    #     context = super().get_context_data(**kwargs)                     
    #     return context


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
    