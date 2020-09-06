from django.shortcuts import render,HttpResponse,redirect
from django.core.mail import send_mail
from django.conf import settings
from .models import Contact
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from blog.models import Post
from django.contrib.auth.models import User
# Create your views here.
def home(request):

    return render(request,'home/index.html')
def about(request):
    return render(request,'home/about.html')
def contact(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        socialmedia=request.POST['socialmedia']
        content=request.POST['content']

        if len(name)<2 or len(email)<5 or len(phone)<6 or len(content)<4:
            messages.error(request, ' Please enter valid details')
        else:
            contact=Contact(name=name,email=email,phone=phone,content=content,socialmedia=socialmedia)
            contact.save()
            messages.success(request, ' Thank you, We will reach you ASAP')
    return render(request,'home/contact.html')


def search(request):
    query=request.GET['query']
    allPostsT=Post.objects.filter(title__icontains=query)
    allPostsC=Post.objects.filter(content__icontains=query)
    allPosts=allPostsT.union(allPostsC)
    params={'allPosts':allPosts, 'query':query}
    return render(request,'home/search.html',params)
def programming(request):
    allPosts=Post.objects.filter(category__icontains='programming')
    params={'allPosts':allPosts}
    return render(request,'home/programming.html',params)
def hacking(request):
    allPosts=Post.objects.filter(category__icontains='hacking')
    params={'allPosts':allPosts}
    return render(request,'home/hacking.html',params)

def terms(request):
    return render(request,'home/terms.html')
def resources(request):
    return render(request,'home/resources.html')
def privacy(request):
    return render(request,'home/privacy.html')


def handleSignup(request):

    if request.method == 'POST':
        #Get the post parameters
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        
        #Check for wrong input
        if len(username)<4 or len(username)>15:
                messages.warning(request," Username must be greater than 3 characters and less than 15 characters.")
                return redirect('home')
        if not username.isalnum():
                messages.warning(request," Username should only contain letters and numbers.")
                return redirect('home')
        if User.objects.filter(username = request.POST['username']).exists():
                messages.warning(request,'You Got The Error as the username already exits. Try unique username')
                return redirect('home')
        if pass1 != pass2:
                messages.warning(request," Passwords did not Match.")
                return redirect('home')



        # create the user
        myuser=User.objects.create_user(username,email,pass1)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save()
        # # send_mail(subject, message, from_email,to_list, fail_silently=True)
        messages.success(request," Your Account has been created. We welcome you to Mad About Hacking.😄")
        return redirect('home')

    else:
        return HttpResponse(" Some Error Occured! Please Try Again😭")

def handleLogin(request):

        if request.method == 'POST':
            #Get the post parameters
            loginusername=request.POST['loginusername']
            loginpass=request.POST['loginpass']

            user=authenticate(username=loginusername,password=loginpass)

            if user is not None:
                login(request,user)
                messages.success(request,' Successfully Logged In😉')
                return redirect('home')
            else:
                messages.error(request,' Cannot Authenticate! Invald Username/Password😣')
                return redirect('home')

        else:
            return HttpResponse("Page not found-404")

def handleLogout(request):
    logout(request)
    messages.success(request, " Logged Out Successfully.😊")
    return redirect('home')

