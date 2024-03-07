from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response

from .forms import FieldDockForm
from .models import FieldComponent
from .serializers import FieldComponentSerializer


class FieldComponentViewSet(viewsets.ModelViewSet):
    queryset = FieldComponent.objects.all()
    serializer_class = FieldComponentSerializer
    http_method_names = ['get', 'post']

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
            form.save()
            messages.success(request, 'FieldComponent added successfully.')
            return redirect('dashboard')
        else:
            messages.error(request, 'Error in the form submission. Please check the data.')

    else:
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
    superusers = User.objects.filter(is_superuser=True)

    field_components = FieldComponent.objects.all()

    return render(request, 'dashboard.html', {'superusers': superusers, 'field_components': field_components})


def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('login')


class AdminLoginView(APIView):
    def post(self, request, format=None):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user is not None and user.is_staff:
            return Response({'message': 'Admin login successful', 'username': user.username})
        else:
            return Response({'message': 'Invalid credentials or not an admin'}, status=status.HTTP_401_UNAUTHORIZED)
