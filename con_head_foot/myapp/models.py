from django.db import models
import os
from django.conf import settings


# Create your models here.

class College(models.Model):
    cname = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "College"

    def __str__(self):
        return self.cname


class Student(models.Model):
    roll_nm = models.IntegerField(unique=True)
    sname = models.CharField(max_length=11)
    email = models.EmailField()
    mobile = models.CharField(max_length=11)
    add_date = models.DateField(auto_now_add=True)
    # college = models.ForeignKey(College, on_delete=CASCADE)
    college = models.ForeignKey(College, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Student"

    def __str__(self):
        return f"{self.sname} ({self.roll_nm})"


# register form

class Register(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    address = models.TextField()
    gender = models.CharField(max_length=10, default=None)
    mobile = models.BigIntegerField()
    password = models.CharField(max_length=20)
    country = models.CharField(max_length=20, null=True)
    state = models.CharField(max_length=20, null=True)
    city = models.CharField(max_length=20, null=True)
    profile_image = models.ImageField(upload_to="profile_photos/")

    # File =models.FileField(upload_to="media/profile_file",default="")

    class Meta:
        verbose_name_plural = "Register"   #admin page vr name kasa pahije

    def __str__(self):
        return f"{self.firstname} ({self.state})"

    # def save(self, *args, **kwargs):
    #     if self.pk:
    #         try:
    #             existingUser = Register.objects.get(pk=self.pk)
    #             if existingUser.profile_image and existingUser.profile_image != self.profile_image:
    #                 if os.path.isfile(existingUser.profile_image.path):
    #                     try:
    #                         os.remove(existingUser.profile_image.path)
    #                     except Exception:
    #                         pass  # Optionally log the error
    #         except Register.DoesNotExist:
    #             pass  # Object does not exist, no image to remove
    #
    #     super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):  # delete madhala images delete karanyasathi
        if self.profile_image:
            if os.path.isfile(self.profile_image.path):
                os.remove(self.profile_image.path)
        super().delete(*args, **kwargs)



# Contact Page


class Contactpages(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.BigIntegerField()
    location = models.CharField(max_length=50)
    message = models.TextField()



    class Meta:
        verbose_name_plural = "Contact"   #admin page vr name kasa pahije
    def __str__(self):
        return f"{self.name} ({self.phone})"




