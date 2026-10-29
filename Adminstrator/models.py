from django.db import models

class tbl_district(models.Model):
    district_name=models.CharField(max_length=30)

class tbl_category(models.Model):
    category_name=models.CharField(max_length=30)

class tbl_adminregistration(models.Model):
    adminregistration_name=models.CharField(max_length=30)
    adminregistration_contact=models.CharField(max_length=30)
    adminregistration_email=models.CharField(max_length=30)
    adminregistration_password=models.CharField(max_length=30)

class tbl_brand(models.Model):
    brand_name=models.CharField(max_length=30)

class tbl_type(models.Model):
    type_name=models.CharField(max_length=30)

class tbl_place(models.Model):
    place_name=models.CharField(max_length=20)
    place_pincode=models.CharField(max_length=20)
    district=models.ForeignKey(tbl_district,on_delete=models.CASCADE)

class tbl_subcategory(models.Model):
    sub_name=models.CharField(max_length=20)
    category=models.ForeignKey(tbl_category,on_delete=models.CASCADE)

class tbl_company(models.Model):
    company_name=models.CharField(max_length=30)


class tbl_model(models.Model):
    company=models.ForeignKey(tbl_company,on_delete=models.CASCADE)
    model_name=models.CharField(max_length=20)

class tbl_body(models.Model):
    body_name=models.CharField(max_length=30)

class tbl_door(models.Model):
    door_value=models.CharField(max_length=30)

class tbl_seat(models.Model):
    seat_value=models.CharField(max_length=30)

class tbl_fuel(models.Model):
    fuel_value=models.CharField(max_length=30)

class tbl_engine(models.Model):
    engine_value=models.CharField(max_length=30)

class tbl_transmission(models.Model):
    transmission_value=models.CharField(max_length=30)

class tbl_drivetrain(models.Model):
    drivetrain_type=models.CharField(max_length=30)

class tbl_ownershipcount(models.Model):
    ownershipcount_type=models.CharField(max_length=30)

class tbl_year(models.Model):
    year_value=models.CharField(max_length=30)

