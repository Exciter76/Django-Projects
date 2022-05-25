from django import forms
from .models import PostContact

"""
    Assign the contacts to the model and get the required fields.
    Note: owner and created are not listed as they will be set
    by their views.
"""


class PostForm(forms.ModelForm):
    class Meta:
        model = PostContact
        fields = ('first_name', 'last_name', 'address1', 'address2', 'email', 'phone_number',
                  'mobile_number', 'notes')
