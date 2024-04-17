from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, HttpResponse
from mainsite.models import *
from users.models import User

global cartList
cartDict = {}
global quantity
quantity =  1
#ajax to handle requests between server and client withoyut needing to refresh page
def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def Home(request):
    if request.method == 'GET':
        productObjs = Products.objects.all()
        context = {'products':productObjs}
        return render(request, 'index.html', context) #show the user the homepage

#view for about page
def about(request):
    if request.method == 'GET':
        return render(request, 'about.html')

#view for contact page
def contact(request):
    if request.method == 'GET':
        return render(request, 'contact.html')

#view for products page
def products(request):
    if request.method == 'GET':
        return render(request, 'products.html')

#view for single product
def singleProduct(request, id):
    if request.method == 'GET':
        productObj = Products.objects.get(id=id)
        context = {'product':productObj}
        return render(request, 'single-product.html', context)

#view for adding to cart
def add_cart(request, id):
    if request.method == "GET":
        cartDict[id]  = 1 #assign id of item and quantity to session dict
        global quantity
        quantity = 1
        send_email('Add To Cart', 'An item was added to cart', int(request.session['uid']))
        return redirect('mainsite:view-cart')
    if request.method == 'POST':
        #update quantity in cartDict
        cartDict[id] = int(cartDict[id]) +1
        quantity = int(cartDict[id]) +1
        send_email('Add To Cart', 'An item was added to cart', int(request.session['uid']))
        return redirect('mainsite:view-cart')

#view to remove quantity of item from cart
def remove_item(request, id):
    if request.method == 'POST':
        #update quantity in cartDict
        cartDict[id] = int(cartDict[id])  -1
        quantity = int(cartDict[id]) -1
        send_email('Remove item', 'An item was removed from the cart', int(request.session['uid']))
        return redirect('mainsite:view-cart')

#view to handle updating cart items
def update(request, id):
    if request.method == 'POST':
        #update quantity in cartDict
        cartDict[id] = int(request.POST['quantity'])
        quantity = int(request.POST['quantity'])
        send_email('Update To Cart', 'An update to cart was made', int(request.session['uid']))
        return redirect('mainsite:view-cart')
        
#function to send email
def send_email(subject,message, uid):
  #imports to facilitate email feature
  import smtplib, ssl, email
  from email.mime.multipart import MIMEMultipart #to facilitate the sending of non-ascii type messages over the internet
  from email.mime.text import MIMEText #to enable sending plain text emails
  #email address of program
  sender = "inventpro01@gmail.com"
  #app password allows us use gmail without having to login and send email to the users
  appPassword = 'povsxbcsdrfueqac'
  receiver = User.objects.get(id=uid).emailAddr
  #create message object
  msg = MIMEMultipart()
  msg['Subject'] = subject
  msg['From'] = sender
  msg['To'] = receiver
  body = message
  msg.attach(MIMEText(body, 'plain'))
  try:
    #send message via a local smtp server
    #create a secured session with gmail's SMTP server to send email
    with  smtplib.SMTP("smtp.gmail.com", 587) as server:
      
      #start TLS for security reasons 
      server.starttls()
      #login to server
      server.login(sender, appPassword)
      #send email to recepient
      server.send_message(msg)
      print('Email sent successfully')
  except Exception as e:
    print(e)
    print('An error occurred sending email')
    return

#view for viewing cart
def view_cart(request):
    if request.method == 'GET':
        cartItms = []
        #check whether items are in cart
        try:
            for itm in cartDict.keys():
                itmObj = Products.objects.get(id=int(itm))
                cartItms.append(itmObj)
        except Exception as e:
            print(e)
            return HttpResponse('<h11>An error occurred</h1>')
        context = {'cartItms': cartItms, 'quantDict':cartDict, 'quantity':cartDict[cartItms[0].id]}
        print(cartDict)
        return render(request, 'viewcart.html', context)