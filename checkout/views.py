from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from .models import Order, OrderLineItem

from products.models import Product
from profiles.models import UserProfile
from profiles.forms import UserProfileForm
from bag.contexts import bag_contents

import stripe
import json

def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    current_bag = bag_contents(request)
    total = current_bag['grand_total']
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

    order_form = OrderForm()

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51QfniI09sax9mVybLbF2PsmBS0dh35BDiPaZb1nRPBRKkVuDcQ57QkeyfTzDOWW6yv9jXFe9VR8f0VxkGLkw4r4u00AfTYk7Iv',
        'client_secret': 'intent.client_secret',
    }

    return render(request, template, context)

    def checkout_success(request, order_number):
        """Handle successful checkouts"""
        save_info = request.session.get('save_info')
        order = get_object_or_404(Order, order_number=order_number)

        if request.user.is_authenticated:
            profile = UserProfile.objects.get(user=request.user)
            # Attach the user's profile to the order
            order.user_profile = profile
            order.save()

            # Save the user's info
            if save_info:
                 profile_data = {
                    'default_phone_number': order.phone_number,
                    'default_country': order.country,
                    'default_postcode': order.postcode,
                    'default_town_or_city': order.town_or_city,
                    'default_street_address1': order.street_address1,
                    'default_street_address2': order.street_address2,
                    'default_county': order.county,
            }
            user_profile_form = UserProfileForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()

    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')

    if 'bag' in request.session:
        del request.session['bag']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
