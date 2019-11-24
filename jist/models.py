from django.db import models

# Create your models here.
class users(models.Model):
    uname=models.CharField(max_length=255)
    pword=models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Users'


class Feedback(models.Model):
    name = models.CharField(max_length=100)
    cmnt = models.CharField(max_length=1024)
    rating=models.CharField(max_length=255)
    datetime = models.DateTimeField(auto_now=True)


class StuDetails(models.Model):
    uname = models.CharField(max_length=255)
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    gender = models.CharField(max_length=20)
    image = models.ImageField(upload_to='media/')
    phone_no = models.CharField(max_length=12)
    email = models.EmailField(max_length=254)
    addr = models.CharField(max_length=50)
    semester = models.IntegerField()
    department = models.CharField(max_length=20)
    roll_no = models.CharField(max_length=20)
    verified= models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'StuDetails'



