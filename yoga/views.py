from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import userinfo, Yoga
a=0
# Create your views here.
def homepage(request):
    return render(request, "homepage1.html")

def login(request):
    if request.method=="POST" :
        username1 = request.POST.get('username')
        password1 = request.POST.get('password')
        try:
            
            users = userinfo.objects.get(username = username1)
            # currentuser = userinfo.objects.get(username = username1)
            password = users.password
            if password1==password:
                a=1
                return HttpResponseRedirect('http://127.0.0.1:8000/dashboard/')
            
            else: 
                return HttpResponse("Wrong Password")
               
        except:
            return HttpResponse('No User Found, Please create a new account')
        
    else:
        return render(request, 'login.html')
    
    
def signup(request):
    if request.method=='POST':
        username1 = request.POST.get('username')  
        email = request.POST.get('email')
        password = request.POST.get('password')
        checkpassword = request.POST.get('checkpassword')
        if password==checkpassword:
            post = userinfo()
            post.username = username1
            post.email = email
            post.password = password
            post.save()
            return HttpResponseRedirect('http://127.0.0.1:8000/dashboard/')
        
        else:
            return HttpResponse('Passwords Dont Match')   
                
    else:
        return render(request, 'signup.html')
    

def dashboard(request):
    if request.method=='POST':
        yogas = 'null'
        problem1 = request.POST.get('yogasearch')
        yogas = Yoga.objects.filter(problem = problem1)
        if yogas!='null':
            return render(request, 'yoga.html', {'yogas': yogas} )
        else:
            return HttpResponse('No Yoga Found')
    
    else:
        return render(request, 'dashboard.html')
    
def displayImage(request, name1):
    yoga = Yoga.objects.get(name=name1)
    image = yoga.picture
    return render(request, {image})
        