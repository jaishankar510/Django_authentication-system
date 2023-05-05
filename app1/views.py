from django.shortcuts import render, HttpResponse, redirect

from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required

from .forms import CustomerForm

# Create your views here.
@login_required(login_url="login")
def home(request):
    return render(request, "home.html")


def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        pass1 = request.POST.get("password1")
        pass2 = request.POST.get("password2")
        
        if pass1 != pass2:
            return HttpResponse("Your password and confirm password not same")
        else:    
            my_user = User.objects.create_user(username,email,pass1)
            my_user.save()
        
            return redirect("login")
        #return HttpResponse("User create seccussfully")
        #print(uname,email,pass1,pass2)
        
        
    return render(request, 'signup.html')

def login(request):
    if request.method == "POST":
        username= request.POST.get("username")
        pass1 = request.POST.get("pass")
       # print(username,pass1)
        user = authenticate(request, username=username, password = pass1)
        if user is not None:
     #       login(request, user)
            return redirect('home')
        else:
            return HttpResponse("Your user and password invaild!!!")
       
    return render(request, 'login.html')


def Logout(request):
    logout(request)
    return redirect('login')


def index(request):
    form= CustomerForm()
    if request.method == 'POST':
        print(request.POST)
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'index.html', context)

