from django.shortcuts import render, redirect
from .forms import ContactForm


def contact(request):
    """Contact form view"""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Thank you {user.name} for contacting us.')
    else:
        form = ContactForm()
    return render(request, 'contact/contact.html', {'form': form})
