from django.contrib import admin
from .models import PostContact

# redundent site.register. kept here in the case of a revert
#admin.site.register(PostContact)

@admin.register(PostContact)
class postAdmin(admin.ModelAdmin):
    """
    Admin has a brief display of our contacts. Simply display the fields first name, last name, when it was
    created and who created the contact(owner or logged in user). Let the user search for a contact
    by last name and order the display by ascending order of last name.

    Not using raw_id because the default in this case doesn't cause much of an overhead.
    """
    list_display = ('first_name', 'last_name','created','owner')
    search_fields = ['last_name']
    ordering = ['last_name']


