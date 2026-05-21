from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.core.paginator import Paginator
from .models import FarmerData
from .forms import UserRegistrationForm, FarmerDataForm, CustomLoginForm

def is_admin(user):
    return user.is_staff

def home(request):
    if request.user.is_authenticated:
        return redirect('user_dashboard')
    approved_data = FarmerData.objects.filter(is_approved=True)[:6]
    return render(request, 'home.html', {'approved_data': approved_data})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful! Welcome to E-Krushi Platform.')
            return redirect('user_dashboard')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def user_dashboard(request):
    user_data = FarmerData.objects.filter(user=request.user)
    return render(request, 'user/dashboard.html', {'user_data': user_data})

@login_required
def add_farmer_data(request):
    if request.method == 'POST':
        form = FarmerDataForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            farmer_data = form.save(commit=False)
            farmer_data.user = request.user
            farmer_data.save()
            messages.success(request, 'Agricultural data submitted successfully! It will be reviewed by admin.')
            return redirect('user_dashboard')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = FarmerDataForm(user=request.user)
    return render(request, 'user/add_data.html', {'form': form})

@user_passes_test(is_admin)
def edit_farmer_data(request, pk):
    farmer_data = get_object_or_404(FarmerData, pk=pk)
    if request.method == 'POST':
        form = FarmerDataForm(request.POST, request.FILES, instance=farmer_data)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data updated successfully!')
            return redirect('admin_dashboard')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = FarmerDataForm(instance=farmer_data)
    return render(request, 'admin/edit_data.html', {'form': form, 'farmer_data': farmer_data})

@user_passes_test(is_admin)
def admin_dashboard(request):
    all_data = FarmerData.objects.all()
    paginator = Paginator(all_data, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'admin/dashboard.html', {'page_obj': page_obj})

@user_passes_test(is_admin)
def approve_data(request, pk):
    farmer_data = get_object_or_404(FarmerData, pk=pk)
    farmer_data.is_approved = True
    farmer_data.save()
    messages.success(request, f'Data for {farmer_data.farmer_name} approved!')
    return redirect('admin_dashboard')

def public_data(request):
    approved_data = FarmerData.objects.filter(is_approved=True)
    paginator = Paginator(approved_data, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'public_data.html', {'page_obj': page_obj})

def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('login')