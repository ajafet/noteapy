from django import forms
from django.forms import ModelForm, TextInput, Textarea
from main.models import User
from django.utils.translation import gettext_lazy as _

class UpdateUserForm(ModelForm):

    use_required_attribute = False

    class Meta: 
        model = User 
        fields = ['username', 'name', 'occupation']
        labels = {
            "username": _("Username "), 
            "name": _("Name "),
            "occupation": _("Occupation "), 
        }
        widgets = {
            "username": TextInput(attrs={"class": "form-control", "placeholder": "Enter Username Here"}), 
            "name": TextInput(attrs={"class": "form-control", "placeholder": "Enter Name Here"}),
            "occupation": Textarea(attrs={"class": "form-control", "placeholder": "Enter Occupation Here", "rows": "5"}),
        }
        error_messages = {
            "username": {
                "unique": "Username already exists.", 
            }, 
        }
        