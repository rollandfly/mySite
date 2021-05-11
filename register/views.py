from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout

# Create your views here.
def registerPage(request):
  if request.user.is_authenticated:
    return redirect('/home')
  else:
    form= RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
          form.save()
          user = form.cleaned_data.get('username')
          messages.success(request,'Account was created for '+ user)
          return redirect("/login")
    else:
      form = RegisterForm()

  return render(request, "register/register.html", {"form": form})

def loginPage(request):
  if request.method == 'POST':
    print("Encours de connexion")
    usn = request.POST.get('username')
    psw = request.POST.get('password')
    user = authenticate(request, username= usn, password = psw)
    if user is not None:
      login(request, user)
      return redirect('/')
    else:
      messages.info(request,'Username or Password are incorrect')
      print('not knwo')
      return redirect('')
  context={}
  return render(request,'register/login.html',context)
