from django.shortcuts import render, redirect, reverse
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import get_template
from django.views.generic import TemplateView

from . import forms

def contact_view(request):
    form = forms.ContactForm()

    if request.method == "POST":
        form = forms.ContactForm(request.POST)

        if form.is_valid():
            name = request.POST.get("name")
            email = request.POST.get("email")
            message = request.POST.get("message")

            subject = 'Contact Form Received'
            from_email = settings.DEFAULT_FROM_EMAIL
            to_email = [settings.DEFAULT_FROM_EMAIL]

            context = {
                'user': name,
                'email': email,
                'message': message
            }

            contact_message = get_template('contact_message.txt').render(context)

            send_mail(subject,contact_message,from_email,to_email,fail_silently=True)
            print(context)
            return redirect('thanks')

    return render(request,'contact.html',{'form':form})

class ThankYouPageView(TemplateView):
    template_name = 'thanks.html'
