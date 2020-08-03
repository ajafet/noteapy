from django.forms import ModelForm, TextInput, Textarea, Select
from main.models import Notes
from django.utils.translation import gettext_lazy as _

class NotesForm(ModelForm):

    use_required_attribute = False

    class Meta: 
        model = Notes 
        fields = ['title', 'content', 'category']
        labels = {
            "title": _("Title "),
            "content": _("Content "), 
            "category": _("Category Name "), 
        }
        widgets = {
            "title": TextInput(attrs={"class": "form-control", "placeholder": "Enter Title Here"}),
            "content": Textarea(attrs={"class": "form-control", "placeholder": "Enter Content Here"}), 
            "category": Select(attrs={"class": "form-control"}), 
        }

    def is_valid(self):
        result = super().is_valid()

        # Append CSS Error Class to Highlight Inputs Red
        for x in (self.fields if '__all__' in self.errors else self.errors):
            attrs = self.fields[x].widget.attrs
            attrs.update({'class': attrs.get('class', '') + ' is-invalid'})

        return result
