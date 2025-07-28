from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout
from .models import TravelOption, Booking
from .forms import BookingForm, UserUpdateForm

# Create your views here.
def home(request):
    featured_travels = TravelOption.objects.filter(is_featured=True)[:6]
    return render(request, 'home.html', {'featured_travels': featured_travels})
def travel_list(request):
    options = TravelOption.objects.all()
    return render(request, 'travel_list.html', {'options': options})

@login_required
def book_travel(request, travel_id):
    travel = get_object_or_404(TravelOption, pk=travel_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            seats = form.cleaned_data['number_of_seats']
            if seats <= travel.available_seats:
                total = seats * travel.price
                booking = form.save(commit=False)
                booking.user = request.user
                booking.travel_option = travel
                booking.total_price = total
                booking.save()
                travel.available_seats -= seats
                travel.save()
                return redirect('my_bookings')
    else:
        form = BookingForm()
    return render(request, 'booking_form.html', {'form': form, 'travel': travel})

@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'bookings.html', {'bookings': bookings})

@login_required
def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id, user=request.user)
    if booking.status == 'Confirmed':
        booking.status = 'Cancelled'
        booking.save()
        booking.travel_option.available_seats += booking.number_of_seats
        booking.travel_option.save()
    return redirect('my_bookings')

@login_required
def profile(request):
    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST.get('first_name', '')
        user.last_name = request.POST.get('last_name', '')
        user.email = request.POST.get('email', '')
        user.save()
        return redirect('profile')
    return render(request, 'profile.html')
    #     form = UserUpdateForm(request.POST, instance=request.user)
    #     if form.is_valid():
    #         form.save()
    # else:
    #     form = UserUpdateForm(instance=request.user)
    # return render(request, 'profile.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
