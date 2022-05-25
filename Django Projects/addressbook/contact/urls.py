from django.urls import path
from . import views

#app_name = 'contact' Because this is a sole project, a namespace is not necessary!

"""Default to the contact list page."""
urlpatterns = [
    path('', views.contact_list, name='contact_list'),
    path('contact/<int:pk>/', views.contact_modify,name="contact_modify"),
    path('contact/new/', views.contact_new, name="contact_new"),
    path('contact/delete/<int:pk>/', views.contact_delete, name="contact_delete")
]