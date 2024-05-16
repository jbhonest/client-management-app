from django.shortcuts import redirect, render
from .models import Client
from .forms import ClientForm, ProfileForm, UserRegistrationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm


def index(request):
    return render(request, "clients_app/index.html")


@login_required
def clients_list(request):
    clients = Client.objects.order_by('-id')
    return render(request, "clients_app/clients_list.html", {"clients": clients, 'nbar': 'list'})


@login_required
def clients_create(request):
    form = ClientForm()
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('clients_app:list')
    return render(request, "clients_app/clients_create.html", {"form": form, 'nbar': 'create'})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to a home page or dashboard
                return redirect('index')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()

    return render(request, 'clients_app/login.html', {'form': form, 'nbar': 'login'})


def logout_view(request):
    logout(request)
    return redirect('clients_app:login')  # Redirect to login page after logout


def register_view(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            login(request, user)
            return redirect('index')
    else:
        user_form = UserRegistrationForm()
        profile_form = ProfileForm()
    return render(request, 'clients_app/register.html', {'user_form': user_form, 'profile_form': profile_form, 'nbar': 'register'})
