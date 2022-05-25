from django.db import models
from django.conf import settings

class PostContact(models.Model):

    """Post Contact Class"""

    """ Many contacts can be created per user (Many to one). If the owner is deleted,
    the related or created contact(s) are deleted. Using AUTH_USER_MODEL because we are refering to the user model.
    NOTE: have to decide if 1 go with setting. AUTH_USER_MODEL
    2 go with get_user_model.
    3 go with User (should go with a custom user. django doc says so!)"""
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete='models.CASCADE')

    """Let name, address & email be a character size of 30."""
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    address1 = models.CharField(max_length=30)
    address2 = models.CharField(max_length=30)
    email = models.CharField(max_length=30) #models.EmailField()

    """Phone & mobile number is about 10 characters"""
    phone_number = models.CharField(max_length=16)
    mobile_number = models.CharField(max_length=16)

    """Notes is a large text field of considerable size"""
    notes = models.TextField()

    """The date that this contact was added"""
    created = models.DateField(auto_now_add=True)

    """Inner class Meta so as to 'Order by'. Contact ordering will be ordered by
        the last name of the contact.
    """
    class Meta:
        ordering = ['last_name']

    """Return a human readable form of this object when called. First name and
        last name briefly describe a contact"""
    def __str__(self):
        return self.first_name + " " + self.last_name


