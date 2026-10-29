from django.shortcuts import render,redirect
from Adminstrator.models import *
from Dealer.models import *
from Guest.models import tbl_dealer
from User.models import *

from decimal import Decimal
from django.http import JsonResponse
import pickle
from datetime import datetime
import pandas as pd



model = pickle.load(open("Assets/Model/car_price_model.pkl","rb"))

brand_encoder = pickle.load(open("Assets/Model/brand_encoder.pkl","rb"))
model_encoder = pickle.load(open("Assets/Model/model_encoder.pkl","rb"))
trans_encoder = pickle.load(open("Assets/Model/trans_encoder.pkl","rb"))
owner_encoder = pickle.load(open("Assets/Model/owner_encoder.pkl","rb"))
fuel_encoder = pickle.load(open("Assets/Model/fuel_encoder.pkl","rb"))

def predict_car_price(request):
    if 'did' not in request.session:
        return redirect('Guest:Login')
    companydata=tbl_company.objects.all()
    modeldata=tbl_model.objects.all()
    modelyeardata=tbl_year.objects.all()
    price=None
    if request.method=="POST":

        modelobject=tbl_model.objects.get(id=request.POST.get("model"))
        model_name=modelobject.model_name
        brand=modelobject.company.company_name
        year = int(request.POST.get("sel_modelyear"))
        current_year = datetime.now().year
        age = current_year - year
        km=int(request.POST.get("km"))
        transmission=request.POST.get("sel_Transmission")
        owner=request.POST.get("owner")
        fuel=request.POST.get("fuel")

        brand=brand_encoder.transform([brand])[0]
        model_name=model_encoder.transform([model_name])[0]
        transmission=trans_encoder.transform([transmission])[0]
        owner=owner_encoder.transform([owner])[0]
        fuel=fuel_encoder.transform([fuel])[0]

        input_data=pd.DataFrame([[

            brand,
            model_name,
            age,
            km,
            transmission,
            owner,
            fuel

        ]],columns=['Brand','model','Age','kmDriven','Transmission','Owner','FuelType'])

        prediction=model.predict(input_data)

        price=" ₹ "+str(int(prediction[0]))

    return render(request,"Dealer/PricePrediction.html",{"price":price,'companydata':companydata,'Modelyear':modelyeardata})

def HomePage(request):
    if 'did' not in request.session:
        return redirect('Guest:Login')
    dealerdata=tbl_dealer.objects.get(id=request.session['did'])
    return render(request,'Dealer/HomePage.html',{'dealer':dealerdata})



def MyProfile(request):
    if 'did' not in request.session:
        return redirect('Guest:Login')
    dealerdata=tbl_dealer.objects.get(id=request.session['did'])
    return render(request,'Dealer/MyProfile.html',{'dealer':dealerdata})

def EditProfile(request):
    if 'did' not in request.session:
        return redirect('Guest:Login')
    dealerdata=tbl_dealer.objects.get(id=request.session['did'])
    if request.method=="POST":
        dealerdata.dealer_name=request.POST.get("txt_name")
        dealerdata.dealer_email=request.POST.get("txt_email")
        dealerdata.dealer_contact=request.POST.get("txt_contact")
        dealerdata.dealer_address=request.POST.get("txt_address")
        dealerdata.save()
        return render(request,"Dealer/Myprofile.html",{'msg':"profile updated"})
    
    return render(request,'Dealer/EditProfile.html',{'dealer':dealerdata})

def ChangePassword(request):
    if 'did' not in request.session:
        return redirect('Guest:Login')
    dealer=tbl_dealer.objects.get(id=request.session['did'])
   
    if request.method=='POST':
        oldpassword=request.POST.get("txt_oldpsw")
        newpassword=request.POST.get("txt_newpsw")
        retypepassword=request.POST.get("txt_retypepsw")

        if dealer.dealer_password==oldpassword:
            if newpassword==retypepassword:
                dealer.dealer_password=newpassword
                dealer.save()
                return render(request,"Dealer/MyProfile.html",{"msg":"password change successfully"})
            else:
                return render(request,"Dealer/ChangePassword.html",{"msg":"new password do not mach"})
        else:
            return render(request,'Dealer/ChangePassword.html',{"msg":"old password incorrect"})
    else:
        return render(request,"Dealer/ChangePassword.html")

def ajaxmodel(request):
    did=request.GET.get("did")
    model=tbl_model.objects.filter(company=did)
    return render(request, 'Dealer/Ajaxmodel.html',{'model':model})       



def AddVehicle(request):
    if 'did' not in request.session:
        return redirect('Guest:Login')
  
    dealer_id = request.session.get('did')
    if not dealer_id:
        dealer_id = 1

    addvehicle_data = tbl_vehicle.objects.all()
    company = tbl_company.objects.all()
    model = tbl_model.objects.all()
    bodytype = tbl_body.objects.all()
    engine = tbl_engine.objects.all()
    seat = tbl_seat.objects.all()
    door = tbl_door.objects.all()
    fuel = tbl_fuel.objects.all()
    transmission = tbl_transmission.objects.all()
    drivetrain = tbl_drivetrain.objects.all()
    ownershipcount = tbl_ownershipcount.objects.all()
    year = tbl_year.objects.all()

    if request.method == "POST":
   
        current_dealer, created = tbl_dealer.objects.get_or_create(
            id=dealer_id,

        )
        
        comid = tbl_model.objects.get(id=request.POST.get("sel_model"))
        companys = tbl_company.objects.get(id=request.POST.get("sel_company"))
        years = tbl_year.objects.get(id=request.POST.get("sel_year"))
        bodytypes = tbl_body.objects.get(id=request.POST.get("sel_body"))
        engines = tbl_engine.objects.get(id=request.POST.get("sel_engine"))
        seats = tbl_seat.objects.get(id=request.POST.get("sel_seat"))
        doors = tbl_door.objects.get(id=request.POST.get("sel_door"))
        fuels = tbl_fuel.objects.get(id=request.POST.get("sel_fuel"))
        transmissions = tbl_transmission.objects.get(id=request.POST.get("sel_transmission"))
        ownershipcounts = tbl_ownershipcount.objects.get(id=request.POST.get("sel_ownership"))
        drivetrains = tbl_drivetrain.objects.get(id=request.POST.get("sel_drive"))
        
        tbl_vehicle.objects.create(
            dealer=current_dealer, 
            vehicle_company=companys,
            vehicle_model_name=comid,
            vehicle_bodytype=bodytypes,
            vehicle_engine_configuration=engines,
            vehicle_seating_capacity=seats,
            vehicle_door_count=doors,
            vehicle_fuel_type=fuels,
            vehicle_transmission_type=transmissions,
            vehicle_drive_train=drivetrains,
            vehicle_ownership_count=ownershipcounts,
            year_count=years,
            vehicle_engine_capacity=request.POST.get("txt_engcapacity"),
            vehicle_power=request.POST.get("txt_power"),
            vehicle_torque=request.POST.get("txt_torque"),
            vehicle_mileage=request.POST.get("txt_milage"),
            vehicle_odometer_count=request.POST.get("txt_odometer"),
            registration_no=request.POST.get("txt_registration"),
            vehicle_price=request.POST.get("txt_price"),
            vehicle_re=request.FILES.get("file_vehiclerc"),
            vehicle_photo=request.FILES.get("file_vehiclephoto"),
            insurance=request.FILES.get("file_insurance"),
        )
        return redirect("Dealer:AddVehicle")

    return render(request, 'Dealer/AddVehicle.html', {
        'addvehicle': addvehicle_data, 'model': model, 'company': company, 
        'bodytype': bodytype, 'engine': engine, 'seat': seat, 'door': door, 
        'fuel': fuel, 'transmission': transmission, 'drivetrain': drivetrain, 
        'ownershipcount': ownershipcount, 'year': year
    })


def Myvehicle(request):
    if 'did' not in request.session:
        return redirect('Guest:Login')
    Myvehicle_data = tbl_vehicle.objects.all()
    return render(request, 'Dealer/Myvehicle.html', {'addvehicle': Myvehicle_data})

def vehicledelete(request,id):
    tbl_vehicle.objects.get(id=id).delete()
    return redirect("Dealer:Myvehicle")


def Gallery(request,id):
    if 'did' not in request.session:
        return redirect('Guest:Login')
    gallery_data=tbl_gallery.objects.filter(vehicle=id)
    if request.method=='POST':
        gallery=request.FILES.get("file_photo")
        tbl_gallery.objects.create(
            gallery=request.FILES.get("file_photo"),
            vehicle=tbl_vehicle.objects.get(id=id)

        )
        return redirect("Dealer:Myvehicle")
    else:
        return render(request,'Dealer/Gallery.html',{'data':gallery_data})


def gallerydelete(request,id):
    tbl_gallery.objects.get(id=id).delete()
    return redirect("Dealer:Gallery")

def ViewBooking(request):
    if 'did' not in request.session:
        return redirect('Guest:Login')
    booking_data = tbl_booking.objects.filter()
    return render(request, 'Dealer/ViewBooking.html',{"viewbooking":booking_data})


def bookingaccept(request,bid):
    accdata=tbl_booking.objects.get(id=bid)
    accdata.booking_status = 1
    accdata.save()
    return render(request,'Dealer/ViewBooking.html',{'msg':'accept'})

def bookingreject(request,bid):
    rejdata=tbl_booking.objects.get(id=bid)
    rejdata.booking_status = 2
    rejdata.save()
    return render(request,'Dealer/ViewBooking.html',{'msg':'reject'})

def Logout(request):
    if 'did' not in request.session:
        return redirect('Guest:Login')
    del request.session['did']
    return redirect('Guest:Login')
