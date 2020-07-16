from django import forms
from django.forms import ModelForm, TextInput, Textarea
from main.models import User
from django.utils.translation import gettext_lazy as _

class UpdateUserForm(ModelForm):

    use_required_attribute = False

    new_password = forms.CharField(label="New Password ", widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Enter New Password"}), required=False)
    confirm_password = forms.CharField(label="Confirm Password ", widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Enter Password to Confirm"}), required=False)

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

    def clean(self): 
        new_password = self.cleaned_data.get("new_password")
        confirm_password = self.cleaned_data.get("confirm_password")

        if new_password and (len(new_password) < 6): 
            self.add_error("new_password", "New Password must contain at least 6 characters.")

        if new_password and not confirm_password: 
            self.add_error("confirm_password", "Confirm Password must match New Password.")

        if confirm_password and (new_password != confirm_password): 
            self.add_error("confirm_password", "Confirm Password must match New Password.")

        return self.cleaned_data   


    def save(self, commit=True):
        
        user = super(UpdateUserForm, self).save(commit=False)

        # Check If Password Needs to be Updated
        new_password = self.cleaned_data.get("new_password")
        confirm_password = self.cleaned_data.get("confirm_password")

        if new_password and (len(new_password) >= 6):
            if confirm_password and (new_password == confirm_password):
                user.set_password(self.cleaned_data["confirm_password"])        
                
        # Update User Information 
        if commit:
            user.save()
        return user  
