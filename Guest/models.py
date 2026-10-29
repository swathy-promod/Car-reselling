from django.db import models
from Adminstrator.models import *

class tbl_user(models.Model):
    user_name=models.CharField(max_length=20)
    user_email=models.CharField(max_length=20)
    user_contact=models.CharField(max_length=20)
    user_address=models.CharField(max_length=20)
    user_gender=models.CharField(max_length=20)
    user_password=models.CharField(max_length=20)
    user_photo=models.FileField(upload_to="Assets/User/photo")
    user_proof=models.FileField(upload_to="Assets/User/photo")
    place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)
    user_status=models.IntegerField(default=0)
    
class tbl_dealer(models.Model):
    dealer_name=models.CharField(max_length=20)
    dealer_contact=models.CharField(max_length=20)
    dealer_email=models.CharField(max_length=20)
    dealer_password=models.CharField(max_length=20)
    dealer_address=models.CharField(max_length=20)
    dealer_place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)
    dealer_status=models.IntegerField(default=0)
    established_date=models.DateField(auto_now_add=True)
    owner_name=models.CharField(max_length=20)
    owner_contact=models.CharField(max_length=20)
    owner_photo=models.FileField(upload_to="Assets/VehicledealerRegistration/photo")
    owner_proof=models.FileField(upload_to="Assets/VehicledealerRegistration/photo")
    licence_proof=models.FileField(upload_to="Assets/VehicledealerRegistration/photo")
    dealer_logo=models.FileField(upload_to="Assets/VehicledealerRegistration/photo")
