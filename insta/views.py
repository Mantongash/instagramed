from django.shortcuts import render, redirect
from .forms import UserReagisterForm
from django.contrib import messages

# Create your views here.
def index(request):
  if request.method == "POST":
    form=UserReagisterForm(request.POST)
    if form.is_valid():
      form.save()
      username = form.cleaned_data.get("username")
      messages.success(request, ("Account for {} has been created successfully").format(username))
      return redirect("login")
  else:
      form=UserReagisterForm()
  return render(request, "insta/index.html",{"form":form})
