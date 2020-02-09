from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.
def index(request):
  if request.method == "POST":
    form=UserCreationForm(request.POST)
    if form.is_valid:
      username = form.cleaned_data.get("username")
      messages.success(request, f("Account for {username} has been created successfully"))
      return redirect("insta-home")
  else:
  form=UserCreationForm()
  return render(request, "insta/index.html",{"form":form})
