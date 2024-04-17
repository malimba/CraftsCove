from django.shortcuts import render, redirect, HttpResponse
from werkzeug.security import check_password_hash
from django.core.exceptions import ObjectDoesNotExist
from .models import User
# Create your views here.

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            userObj = User.objects.get(username=username)
            passwordHash = userObj.password
             #validate whether password correct
            if check_password_hash(passwordHash, password):
                #set session to logged in
                request.session['isLoggedIn'] = True
                request.session['uid'] = userObj.id
                #redirect user indictating user is logged in
                return redirect('mainsite:Home') #redirect user to homepage
            return HttpResponse('<h1>Password incorrect</h1>')

        except ObjectDoesNotExist:
            print('User does not exist')
            return HttpResponse('<h1>User does not exist, go back to correct credentials</h1>')
       

def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    if request.method == 'POST':
        firstname = request.POST['fname']
        lastname = request.POST['lname']
        username = request.POST['uname']
        emailAddr = request.POST['mail']
        gender = request.POST['gender']
        password = request.POST['pass']
        userObj =   User.objects.create(
            fullname = f'{firstname} {lastname}',
            username = username,
            emailAddr = emailAddr,
            gender = gender,
            password = password
        )
        userObj.hash_password()
        userObj.save()
        return redirect('users:login')