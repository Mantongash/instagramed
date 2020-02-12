from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from insta.forms import ProfileUpdateForm, UserUpdateForm, UploadForm
from django.contrib import messages
from .models import Post

# Create your views here.

def account_home(request):
   posts = Post.objects.all()
   return render(request, "login/home.html", {"posts":posts})

@login_required()
def profile(request):

  return render(request, "login/profile.html")


@login_required()
def edit_profile(request):
  if request.method == "POST":
    u_form = UserUpdateForm(request.POST, instance=request.user)
    p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
    if u_form.is_valid() and p_form.is_valid():
      u_form.save()
      p_form.save()
      messages.success(request, "Profile updated successfully")
      return redirect("edit_profile")

  else:
    u_form = UserUpdateForm(instance=request.user)
    p_form = ProfileUpdateForm(instance=request.user.profile)
  context = {
    "u_form" : u_form,
    "p_form" : p_form
  }
  return render(request, "login/edit_profile.html", context)
  
@login_required()
def upload(request):
 
  if request.method == "POST":
    upload_form = UploadForm(request.POST, request.FILES)
    if upload_form.is_valid():
      upload_form.save()
      return redirect("account_home")
  else:
    upload_form = UploadForm()
    
  
  return render(request, "login/upload.html", {"upload_form":upload_form})
