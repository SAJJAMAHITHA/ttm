import random
import string

from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.http import HttpResponse
from django.shortcuts import render

from django.contrib.auth import authenticate


from  .forms import IntegerDateForm
from.models import *
from django.shortcuts import render,redirect
def registerloginfunction(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        phonenumber=request.POST.get('phonenumber')
        if Register.objects.filter(email=email).exists():
            message1="Email already registered.Choose a differebt email."
            return render(request,'myregisterpage.html',{'message1':message1})
        Register.objects.create(name=name,email=email,password=password,phonenumber=phonenumber)
        return redirect('newhomepage')
    return render(request,'myregister.html')
# Create your views here.
def hello(request):
    return render(request,'firsthtml.html')

def hello1(request):
    return HttpResponse("<center><font color=blue>Welcome to TTM Homepage</font color></center>")
def newhomepage(request):
    return render(request,'newhomepage.html')
def travelpackage(request):
    return render(request,'travelpackage123.html')
def print1(request):
    return render(request,'print_to_console.html')
def print_to_console(request):
    if request.method == "POST":
        User_Input= request.POST['User_Input']
        print(f'User_Input:{User_Input}')
    #return HttpResponse('Form Submitted Successfully')
    a1={'User_Input':User_Input}
    return render(request,'print_to_console.html',a1)




def ran(request):

    return render(request,'random123.html')


def random123(request):
    if request.method == "POST":
        input1=request.POST['input1']
        input2=int(input1)
        result_str=''.join(random.sample(string.digits,input2))
        print(result_str)
        contex={'result_str':result_str}
    return render(request,"random123.html",contex)


def getdate1(request):
    return render(request,'get_date.html')

import datetime
from django.shortcuts import render
def get_date(request):
    if request.method=='POST':
        form=IntegerDateForm(request.POST)
        if form.is_valid():
            integer_value=form.cleaned_data['integer_value']
            date_value=form.cleaned_data['date_value']
            updated_date= date_value + datetime.timedelta(days=integer_value)
            return render(request,'get_date.html',{'updated_date':updated_date})
        else:
            form=IntegerDateForm()
        return render(request,'get_date.html',{'form':form})

def timezfnccall(request):
    return render(request,'pytzexample.html')
def registerfunctioncall(request):
    return render(request,'data.html')

def piechart(request):
    return render(request,'chartform.html')



import matplotlib.pyplot as plt
import numpy as np

def pie_chart(request):
    if request.method == 'POST':
        form = PieChartForm(request.POST)
        if form.is_valid():
            # Process user input
            y_values = [int(val) for val in form.cleaned_data['y_values'].split(',')]
            labels = [label.strip() for label in form.cleaned_data['labels'].split(',')]

            # Create pie chart
            plt.pie(y_values, labels=labels, startangle=90)
            plt.savefig('static/images/pie_chart.png')  # Save the chart image
            img1={'chart_image': '/static/images/pie_chart.png'}
            return render(request, 'chartform.html', img1)
    else:
        form = PieChartForm()
    return render(request, 'chartform.html', {'form': form})

def image(request):
    return render(request,'carousel.html')
import requests
def weatherpagecall(request):
    return render(request,'weather.html')

def weatherlogic(request):
    if request.method == 'POST':
        place = request.POST['place']
        API_KEY = '4bf4f1f952eaece1997a0059877d3dc2'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={place}&appid={API_KEY}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            temperature1= round(temperature - 273.15,2)
            return render(request, 'weather.html',
                          {'city': str.upper(place), 'temperature1': temperature1, 'humidity': humidity})
        else:
            error_message = 'City not found. Please try again.'
            return render(request, 'weather.html', {'error_message': error_message})
def login(request):
    return render(request,'login.html')
def singup(request):
    return render(request,'signup.html')
def login1(request):
    if request.method=='POST':
        username=request.POST['username']
        pass1=request.POST['password']
        user=auth.authenticate(username=username,password=pass1)
        if user is not None:
            auth.login(request,user)
            return render(request,'newhomepage.html')
        else:
            messages.info(request,'Invalid credentials')
            return render(request,'login.html')
    else:
        return render(request,'login.html')
def signup1(request):
    if request.method=="POST":
        username=request.POST['username']
        pass1=request.POST['password']
        pass2=request.POST['password1']
        if pass1==pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'OOPS! Username already taken')
                return render(request,'signup.html')
            else:
                user=User.objects.create_user(username=username,password=pass1)
                user.save()
                messages.info(request,'Account created successfully!')
                return render(request,'login.html')
    else:
            messages.info(request,'Passwprd do not match')
            return render(request,'signup.html')
def logout(request):
    auth.logout(request)
    return render(request,'newhomepage.html')
def contactmail1(request):
    return render(request,'contact.html')
def contactmail(request):
    if request.method == "POST":
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email = request.POST['email']
        comment = request.POST['comment']
        tosend=comment+'------------------------------- This is just the copy of '
        data=contactus(firstname=firstname,lastname=lastname,email=email,comment=comment)
        data.save()
        return HttpResponse("<h1><center>Thank you giving Feedback </center></h1>")




















