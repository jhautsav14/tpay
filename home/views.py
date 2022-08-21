from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required
from .models import (Amenities, Fluid , FluidBooking)

import pyrebase



filename = r'tpay\teapay-6834b-firebase-adminsdk-g39jk-e273f33510.json'


config = {
  'apiKey': "AIzaSyDcbN4xfbwWC6j_ufPTmXGaD0x9izpCCZ8",
  'authDomain': "teapay-6834b.firebaseapp.com",
  'databaseURL': "https://teapay-6834b-default-rtdb.firebaseio.com",
  'projectId': "teapay-6834b",
  'storageBucket': "teapay-6834b.appspot.com",
  'messagingSenderId': "714683864605",
  'appId': "1:714683864605:web:19fbf9cc37b31bf12358f4",
  'measurementId': "G-K6ZE9G52BZ",
  'serviceAccount': 'teapay-6834b-firebase-adminsdk-g39jk-e273f33510.json'
}
firebase=pyrebase.initialize_app(config)
auth = firebase.auth()

# Log the user in
# user = auth.sign_in_with_email_and_password(email, password)

database=firebase.database()


@login_required(login_url="login")
def home(request):
    amenities_objs = Amenities.objects.all()
    fluid_objs = Fluid.objects.all()

    context = {'amenities_objs' : amenities_objs , 'fluid_objs': fluid_objs}

    return render(request , 'home.html' , context)



def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user_obj = User.objects.filter(username = username)

        if not user_obj.exists():
            messages.warning(request, 'Account not found')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        user_obj = authenticate(username = username , password = password)
        if not user_obj:
            messages.warning(request, 'Invalid Credential')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        login(request , user_obj)
        return redirect('/')

        
        
    return render(request, "login.html")

def logout_page(request):
    logout(request)
    return redirect('login')

def register_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        re_password = request.POST.get('re_password')

        user_obj = User.objects.filter(username = username)

        if user_obj.exists():
            messages.warning(request, 'Username already exists')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        if password == re_password:
            user = User.objects.create(username = username)
            user.set_password(password)
            user.save()
            return redirect('login')

        else :
            messages.warning(request, 'Password do not match')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        


    return render(request, "register.html")

@login_required(login_url="login")
def payment(request):
    # if request.method == 'POST':
    #     FluidBooking.objects.create(fluid="Chai", user=request.user)
    #     messages.success(request, 'Payment Done')
        return redirect('/change_db/')

@login_required(login_url="login")
def change_db(request):
    name = database.child('test').child('int').get().val()
    num = database.child('test').child('bool').get().val()
    user = request.user
    up= database.update({'user':str(user)})
    ui = database.child('test').update({'int': 1})


    us = database.child('user').get().val()
    



    FluidBooking(fluid='Chai', user = user).save()

    # return render(request, 'change_db.html', {


    #     "num":num,
    #     "name":name,
    #     "us": us
    # })
    return redirect('orders')

@login_required(login_url="login")
def orders(request):

    user = request.user
    fb = FluidBooking.objects.filter(user=user)
    context = {'user' : user }



    return render(request, 'orders.html', context)