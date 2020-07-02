from django.forms import ModelForm, TextInput
from main.models import Categories
from django.utils.translation import gettext_lazy as _

class CategoryForm(ModelForm):

    use_required_attribute = False

    class Meta: 
        model = Categories 
        fields = ['name']
        labels = {
            "name": _("Category Name "), 
        }
        widgets = {
            "name": TextInput(attrs={"class": "form-control", "placeholder": "Enter Name Here"}), 
        }
