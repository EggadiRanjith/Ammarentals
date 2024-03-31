from django.shortcuts import render ,redirect
from .models import User 
from django.contrib.sessions.models import Session

# Create your views here.
def login_view(request):
   return render(request,'login.html')

from django.shortcuts import render, redirect
from .models import User

def register(request):
    if request.method == 'POST':
        # Retrieve data from the form
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        username = request.POST.get('registerUsername')
        password = request.POST.get('registerPassword')  # In practice, hash the password before saving it

        # Create a new User instance and save it to the database
        user = User(email=email, contact=contact, username=username, password=password)
        user.save()
        request.session['user_email'] = email
        request.session['user_mobile'] = contact
        request.session['user_name'] = username
        # Redirect to a success page or perform other actions
        return redirect('homepage')

    return render(request, 'login.html')  # Replace 'registration_form.html' with your actual template path

def login(request):
    if request.method == 'POST':
        # Retrieve data from the form
        email = request.POST.get('loginUsername')
        password = request.POST.get('loginPassword')

        try:
            user = User.objects.get(email=email)
            # In practice, you should hash the password and compare it securely.
            # You should NEVER store passwords as plain text in the database.
            if user.password == password:
                request.session['user_email'] = user.email
                request.session['user_mobile'] = user.contact
                request.session['user_name'] = user.username
                if user.is_admin==1:
                    request.user = user
                    return redirect('ammarentaladmin')
                else:
                    request.user = user
                    return redirect('homepage')
            else:
                print('Password does not match')
                return render(request, 'login.html')

        except User.DoesNotExist:
            print('User not found')
            return render(request, 'login.html')

    return render(request, 'login.html')

