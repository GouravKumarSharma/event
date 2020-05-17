from django.db import models

# Create your models here.

class farmhouse_detail(models.Model):
    name = models.CharField(max_length=100)
    discription = models.CharField(max_length=1000)
    mobile_no = models.IntegerField(default="")
    email = models.EmailField()
    cover_image = models.ImageField(upload_to="eventapp/images")
    def __str__(self):
        return self.name
class user_login(models.Model):
    u_name=models.CharField(max_length=100)
    email = models.EmailField(default="")
    u_number = models.IntegerField(default="")
    u_image=models.ImageField(upload_to="eventapp/images")
    def __str__(self):
        return self.u_name
