from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail

def contact(request):
    if request.method == "POST":
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        # check if user already made an inquiry
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(user_id=user_id, listing_id=listing_id)
            if has_contacted:
                messages.error(request, "You have already made an inquiry for this listing!")
                return redirect('/listings/'+listing_id)
        else:
            user_email = request.POST["email"]
            has_contacted = Contact.objects.all().filter(email=user_email, listing_id=listing_id)
            messages.error(request, "You have already made an inquiry for this listing!")
            return redirect('/listings/'+listing_id)

        contact = Contact(listing_id=listing_id, listing=listing, name=name, email=email, phone=phone, message=message, user_id=user_id)
        contact.save()

        #send_mail(
        #    'Property Inquiry' + listing,
        #    'There has been an inquiry. Please log in to admin panel for more info!',
        #    'hamro.project.company@gmail.com',
        #    [realtor_email, 'hamro.project.company@gmail.com'],
        #    fail_silently=False
        #)


        messages.success(request, "Your inquiry has been submitted. Realtor will get back soon!")
        return redirect('/listings/'+listing_id)


