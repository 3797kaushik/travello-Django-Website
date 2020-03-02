from django.shortcuts import render , redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.

def register(request):
    print('='*90,request.method )
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        user_name = request.POST['user_name']
        email = request.POST['email']

        password1  = request.POST['password1']
        password2  = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username = user_name).exists():
                messages.info(request,'Username Taken')
                return redirect('register')
            elif User.objects.filter(email = email).exists():
                messages.info(request,'Email Taken')
                return redirect('register')
            else:    
                user = User.objects.create_user(username=user_name,
                                                first_name=first_name,
                                                last_name=last_name,
                                                email=email,
                                                password=password1                                         
                                                )
                user.save()
                print('user created')
        else:
            print('password not matching .. ')
            return redirect('register')
        return redirect('/')

    else:
        return render(request,'register.html')
