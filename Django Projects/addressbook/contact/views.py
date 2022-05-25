from django.shortcuts import render, get_object_or_404, redirect
from .models import PostContact
from .forms import PostForm

"""
   Assign contacts collection to all records of contacts found in the post contact table. 
   Retrieve these records by last name in ascending order.

   render the contacts to the contact list web page. 
"""


def contact_list(request):
    contacts = PostContact.objects.order_by('last_name')

    # Pass down to render that this page is an address book. It can be determined by the
    # request.PATH but a more simpler way is simply pass in a string key,pair
    return render(request, 'contact_list.html', {'contacts': contacts, 'page':'Address Book'})


"""
    create a new contact
    
"""


def contact_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            postcontact = form.save(commit=False)
            postcontact.owner = request.user
            form.save()
            return redirect('contact_list')
    else:
        form = PostForm()

    return render(request, 'contact_detail.html', {'contact': form, 'page':'New Contact'})


"""
    modify an existing contact. Requires the contact id
"""


def contact_modify(request, pk):
    contact = get_object_or_404(PostContact, pk=pk)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=contact)  # pass in the contact to populate the fields on our form

        if form.is_valid():
            post_contact = form.save(commit=False)  # create the model instance but don't save it yet!
            post_contact.owner = request.user
            form.save()
            return redirect('contact_list')
    else:
        form = PostForm(instance=contact)

    return render(request, 'contact_detail.html', {'contact': form, 'page':'Update Contact'})


"""
    Remove a contact. Request is redundant but it must be passed
"""


def contact_delete(request, pk):
    contact = get_object_or_404(PostContact, pk=pk)
    contact.delete()

    return redirect('contact_list')
