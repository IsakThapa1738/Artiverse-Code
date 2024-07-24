from django.shortcuts import render, redirect
from . models import Visitor
from django.contrib.auth.decorators import login_required
from .forms import VisitorForm
from django.db import IntegrityError
from . forms import BillingAddressForm
from . models import BillingAddress
# Create your views here.

@login_required
def artist_profile(request):
    artist = Visitor.objects.get(user=request.user)
    return render(request, 'Artists/artist_profile.html', {'artist': artist})

@login_required
def create_user(request):
    user = request.user
    try:
        visitor = Visitor.objects.get(user=user)
    except Visitor.DoesNotExist:
        visitor = None

    if request.method == 'POST':
        form = VisitorForm(request.POST, request.FILES, instance=visitor)
        if form.is_valid():
            try:
                if visitor:
                    form.save()  # Update existing visitor profile
                else:
                    visitor = form.save(commit=False)
                    visitor.user = user
                    visitor.save()  # Create new visitor profile
                return redirect('user_profile')  # Redirect to a success page
            except IntegrityError:
                return render(request, 'User/create_user.html', {'form': form, 'error': 'Visitor profile could not be created due to a database error.'})
    else:
        form = VisitorForm(instance=visitor)

    return render(request, 'User/create_user.html', {'form': form})

@login_required(login_url='login_view')
def user_profile(request):
    user = request.user
    try:
        profile = Visitor.objects.get(user=user)
    except Visitor.DoesNotExist:
        return redirect('create_user')

    try:
        billing_address = BillingAddress.objects.get(user=user)
    except BillingAddress.DoesNotExist:
        billing_address = None

    context = {
        'profile': profile,
        'billing': billing_address,
    }
    return render(request, 'User/user_profile.html', context)

@login_required
def billing_address(request):
    user = request.user
    try:
        billing_address = BillingAddress.objects.get(user=user)
    except BillingAddress.DoesNotExist:
        billing_address = None

    if request.method == 'POST':
        form = BillingAddressForm(request.POST, instance=billing_address)
        if form.is_valid():
            billing_address = form.save(commit=False)
            billing_address.user = user
            billing_address.save()
            return redirect('user_profile') 
    else:
        form = BillingAddressForm(instance=billing_address)

    return render(request, 'User/billing_det.html', {'form': form})