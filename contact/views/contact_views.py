from django.shortcuts import render, get_object_or_404
from contact.models import Contact
from django.http import Http404

def index(resquest):

    contacts = Contact.objects.filter(show=True).order_by('-id')[:10]

    context = {
        'contacts': contacts,
    }

    return render(
        resquest,
        'contact/index.html',
        context
    )

def contact(resquest, contact_id):

    # single_contact = Contact.objects.filter(pk=contact_id).first()

    single_contact = get_object_or_404(Contact, pk=contact_id)

    # if single_contact is None:
    #     raise Http404()

    context = {
        'contact': single_contact,
    }

    return render(
        resquest,
        'contact/contact.html',
        context
    )