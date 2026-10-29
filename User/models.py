from django.db import models
from Adminstrator.models import *
from Guest.models import*
from Dealer.models import*


class tbl_complaint(models.Model):
    complaint_title=models.CharField(max_length =200)
    complaint_content=models.CharField(max_length=200)
    complaint_date=models.DateField(auto_now_add=True)
    complaint_status=models.IntegerField(default=0)
    complaint_replay=models.CharField(max_length=200)
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE)

class tbl_feedback(models.Model):
    feedback_content=models.CharField(max_length=200)
    feedback_data=models.DateField(auto_now_add=True)
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE)


class tbl_rating(models.Model):
    rating_data=models.IntegerField()
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE)
    user_review=models.CharField(max_length=500)
    dealer=models.ForeignKey(tbl_dealer,on_delete=models.CASCADE)
    datetime=models.DateTimeField(auto_now_add=True)



class tbl_booking(models.Model):
    booking_date = models.DateField(auto_now_add=True)
    booking_amount = models.IntegerField(default=0)
    booking_status = models.IntegerField(default=0)
    user = models.ForeignKey(tbl_user, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(tbl_vehicle, on_delete=models.CASCADE)