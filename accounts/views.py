from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contact


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, "Your are now logged in!")
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid credetials!")
            return redirect('login')

    return render(request, 'accounts/login.html')

def dashboard(request):
    user_contacts = Contact.objects.order_by("-contact_date").filter(user_id=request.user.id)

    context = {"contacts": user_contacts}
    return render(request, 'accounts/dashboard.html', context)

def register(request):
    if request.method == "POST":
        # get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        user_data = {
            "first_name": first_name,
            "last_name": last_name,
            "username": username,
            "email": email,
            "password": password,
        }

        if password == password2:
            # Check username
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already taken!")
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, "Email already in use!")
                    return redirect('register')
                else:
                    # Looks Good (now write to database)
                    user = User.objects.create_user(**user_data)
                    user.save()
                    messages.success(request, "You are now registered. Please log in!")
                    return redirect('login')
        else: 
            messages.error(request, "Password do no match!")
            return redirect('register')

        return redirect('register')
    else:
        return render(request, 'accounts/register.html')

def logout(request):
    if request.method == "POST":
        auth.logout(request)
        messages.success(request, "Your are now logged out!")
        return redirect('index')
