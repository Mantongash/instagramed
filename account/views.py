from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

def account_home(request):
  return render(request, "login/home.html")

@login_required()
def profile(request):
  return render(request, "login/profile.html")
  
