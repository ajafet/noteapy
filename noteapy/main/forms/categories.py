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

    def is_valid(self):
        result = super().is_valid()

        # Append CSS Error Class to Highlight Inputs Red
        for x in (self.fields if '__all__' in self.errors else self.errors):
            attrs = self.fields[x].widget.attrs
            attrs.update({'class': attrs.get('class', '') + ' is-invalid'})

        return result
