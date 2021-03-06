from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.

class Post(models.Model):
  user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
  image = models.ImageField(upload_to="profile_pics")
  caption = models.CharField(max_length=200)



class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  image = models.ImageField(default="profile.jpg", upload_to="profile_pics")

  def __str__(self):
    return ("{} profile").format(self.user.username)

  def save(self, **kwargs):
    super().save()

    img = Image.open(self.image.path)
    if img.height > 300 or img.width > 300:
      output_size = (300, 300)
      img.thumbnail(output_size)
      img.save(self.image.path)
