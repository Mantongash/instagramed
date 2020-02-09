from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def index(request):
  form=UserCreationForm()
  return render(request, "insta/index.html",{"form":form})
