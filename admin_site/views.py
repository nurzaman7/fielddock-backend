# admin_site/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import FieldDockForm  # Import your form
# Import your FieldComponent model
from .models import FieldComponent


# admin_site/views.py
from rest_framework import viewsets
from .serializers import FieldComponentSerializer

class FieldComponentViewSet(viewsets.ModelViewSet):
    queryset = FieldComponent.objects.all()
    serializer_class = FieldComponentSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=201, headers=headers)
        
        


@login_required(login_url='login')
def add_fieldcomponent(request):
    if request.method == 'POST':
        form = FieldDockForm(request.POST)
        if form.is_valid():
            # Save the form data to create a new FieldComponent
            form.save()
            messages.success(request, 'FieldComponent added successfully.')
            return redirect('dashboard')
        else:
            messages.error(request, 'Error in the form submission. Please check the data.')

    else:
        # If it's a GET request, create a new form
        form = FieldDockForm()

    return render(request, 'add_fieldcomponent.html', {'form': form})



def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password. Please try again.')

    return render(request, 'login.html')


@login_required(login_url='login')
def dashboard(request):
    # Retrieve all superusers
    superusers = User.objects.filter(is_superuser=True)

    # Retrieve all FieldComponents
    field_components = FieldComponent.objects.all()

    return render(request, 'dashboard.html', {'superusers': superusers, 'field_components': field_components})
    
    

def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('login')

