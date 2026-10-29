
from django.db import models
from Adminstrator.models import *
from Guest.models import *

class tbl_vehicle(models.Model):
    registration_no = models.CharField(max_length=20)
    vehicle_re = models.FileField(upload_to="Assets/Dealer/photo")
    vehicle_photo = models.FileField(upload_to="Assets/Dealer/photo")
    insurance = models.FileField(upload_to="Assets/Dealer/photo")

    vehicle_company = models.ForeignKey(tbl_company, on_delete=models.CASCADE)
    vehicle_model_name = models.ForeignKey(tbl_model, on_delete=models.CASCADE)
    vehicle_bodytype = models.ForeignKey(tbl_body, on_delete=models.CASCADE)
    vehicle_engine_configuration = models.ForeignKey(tbl_engine, on_delete=models.CASCADE)
    vehicle_seating_capacity = models.ForeignKey(tbl_seat, on_delete=models.CASCADE)
    vehicle_door_count = models.ForeignKey(tbl_door, on_delete=models.CASCADE)
    vehicle_fuel_type = models.ForeignKey(tbl_fuel, on_delete=models.CASCADE)
    vehicle_transmission_type = models.ForeignKey(tbl_transmission, on_delete=models.CASCADE)
    vehicle_drive_train = models.ForeignKey(tbl_drivetrain, on_delete=models.CASCADE)
    vehicle_ownership_count = models.ForeignKey(tbl_ownershipcount, on_delete=models.CASCADE)
    year_count = models.ForeignKey(tbl_year, on_delete=models.CASCADE)
    vehicle_engine_capacity = models.CharField(max_length=20)
    vehicle_power = models.CharField(max_length=20)
    vehicle_torque = models.CharField(max_length=20)
    vehicle_mileage = models.CharField(max_length=20)
    vehicle_odometer_count = models.CharField(max_length=20)
    vehicle_price = models.IntegerField()
    dealer = models.ForeignKey(tbl_dealer, on_delete=models.CASCADE)


class tbl_gallery(models.Model):
    gallery = models.FileField(upload_to="Assets/Dealer/photo")
    vehicle = models.ForeignKey(tbl_vehicle, on_delete=models.CASCADE)