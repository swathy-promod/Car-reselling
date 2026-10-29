from django.shortcuts import render,redirect
from Adminstrator.models import *
from Guest.models import *
from User.models import *

def AdminRegistration(request):
    if 'aid' not in request.session:
        return redirect('Guest:Login')
    adminregistration_data=tbl_adminregistration.objects.all()
    if request.method=="POST":
        name=request.POST.get("txt_name") 
        contact=request.POST.get("txt_contact") 
        email=request.POST.get("txt_email") 
        password=request.POST.get("txt_password") 
        tbl_adminregistration.objects.create(
            adminregistration_name=name,
            adminregistration_contact=contact,
            adminregistration_email=email,
            adminregistration_password=password
        )
        return redirect("Admin:AdminRegistration")
    else:
        return render(request,'Adminstrator/AdminRegistration.html',{'adminregistration':adminregistration_data})

def Category(request):
    if 'aid' not in request.session:
        return redirect('Guest:Login')
    category_data=tbl_category.objects.all()
    if request.method=="POST":
        category=request.POST.get("txt_category")
        tbl_category.objects.create(
            category_name=category
        )
        return redirect("Admin:Category")
    else:
        return render(request,'Adminstrator/Category.html',{'category':category_data})

def District(request):
    if 'aid' not in request.session:
        return redirect('Guest:Login')
    district_data=tbl_district.objects.all()
    if request.method=="POST":
        district=request.POST.get("txt_district")
        tbl_district.objects.create(
            district_name=district
        )
        return redirect("Admin:District")
    else:
        return render(request,'Adminstrator/District.html',{'district':district_data})
    
def Brand(request):
    if 'aid' not in request.session:
        return redirect('Guest:Login')
    brand_data=tbl_brand.objects.all()
    if request.method=="POST":
        brand=request.POST.get("txt_brand")
        tbl_brand.objects.create(
            brand_name=brand
        )
        return redirect("Admin:Brand")
    else:
        return render(request,'Adminstrator/Brand.html',{'brand':'brand_data'})

def Type(request):
    if 'aid' not in request.session:
        return redirect('Guest:Login')
    type_data=tbl_type.objects.all()
    if request.method=="POST":
        ty=request.POST.get("txt_type")
        tbl_type.objects.create(
            type_name=ty
        )
        return redirect("Admin:Type")
    else:
        return render(request,'Adminstrator/Type.html',{'type':type_data})

def Place(request):
    if 'aid' not in request.session:
        return redirect('Guest:Login')
    districtdata= tbl_district.objects.all()
    placedata= tbl_place.objects.all()
    if request.method == "POST":
        name=request.POST.get("txt_place")
        pincode=request.POST.get("txt_pincode")
        disid=tbl_district.objects.get(id=request.POST.get("sel_district"))
        tbl_place.objects.create(place_name=name,place_pincode=pincode,district=disid)
        return redirect("Admin:Place")

    return render(request,'Adminstrator/Place.html',{'districtdata':districtdata,'data':placedata})

def editplace(request,id):
    districtdata= tbl_district.objects.all()
    placedata= tbl_place.objects.all()
    editdata=tbl_place.objects.get(id=id)
    if request.method=='POST':
        editdata.district=tbl_district.objects.get(id=request.POST.get('sel_district'))
        editdata.place_name=request.POST.get('txt_place')
        editdata.place_pincode=request.POST.get('txt_pincode')
        editdata.save()
        return redirect("Admin:Place")
    return render(request,'Adminstrator/Place.html',{'districtdata':districtdata,'editdata':editdata,'data':placedata})
    
def deleteplace(request,id):
    data=tbl_place.objects.get(id=id).delete()
    return redirect("Admin:Place")

def Product(request):
    if 'aid' not in request.session:
        return redirect('Guest:Login')
    return render(request,'Adminstrator/Product.html')

def SubCategory(request):
    if 'aid' not in request.session:
        return redirect('Guest:Login')
    categorydata=tbl_category.objects.all()
    subcategorydata=tbl_subcategory.objects.all()
    if request.method=="POST":
        name=request.POST.get("txt_subcategory")
        subid=tbl_category.objects.get(id=request.POST.get("sel_category"))
        tbl_subcategory.objects.create(sub_name=name,category=subid)
        return redirect("Admin:SubCategory")
    return render(request,'Adminstrator/SubCategory.html',{'categorydata':categorydata,'subcategorydata':subcategorydata})

def UserList(request):
     if 'aid' not in request.session:
        return redirect('Guest:Login')
     UserList=tbl_user.objects.all()
     return render(request,'Adminstrator/UserList.html',{'userlist':UserList})

def HomePage(request):
    if 'aid' not in request.session:
        return redirect('Guest:Login')

    ucount=tbl_user.objects.all().count()
    dcount=tbl_dealer.objects.all().count()
    ccount=tbl_complaint.objects.all().count()
    fcount=tbl_feedback.objects.all().count()
    return render(request, 'Adminstrator/HomePage.html', {
    'ucount': ucount,
    'dcount': dcount,
    'ccount': ccount,
    'fcount': fcount
})

def DealerList(request):
     if 'aid' not in request.session:
        return redirect('Guest:Login')
     DealerList=tbl_dealer.objects.all()
     return render(request,'Adminstrator/DealerList.html',{'dealerlist':DealerList})


def ViewComplaint(request):
    if 'aid' not in request.session:
        return redirect('Guest:Login')
    complaint=tbl_complaint.objects.filter(complaint_status=0)
    reply=tbl_complaint.objects.filter(complaint_status=1)
    return render(request,'Adminstrator/ViewComplaint.html',{'complaint':complaint,'reply':reply})

def Reply(request,id):
    if 'aid' not in request.session:
        return redirect('Guest:Login')
    comp=tbl_complaint.objects.get(id=id)
    if request.method=="POST":
        reply=request.POST.get("txt_rp")
        comp.complaint_replay=reply
        comp.complaint_status=1
        comp.save()
        return redirect("Admin:ViewComplaint")
    return render(request,'Adminstrator/Reply.html')

def Company(request):
    if 'aid' not in request.session:
        return redirect('Guest:Login')
    company_data=tbl_company.objects.all()
    if request.method=="POST":
        company_name=request.POST.get("txt_company")
        tbl_company.objects.create(
            company_name=company_name
        )
        return redirect("Admin:Company")
    else:
        return render(request,'Adminstrator/Company.html',{'company':company_data})

def Model(request):
    if 'aid' not in request.session:
        return redirect('Guest:Login')
    companydata= tbl_company.objects.all()
    modeldata=tbl_model.objects.all()
    if request.method == "POST":
        name=request.POST.get("txt_model")
        comid=tbl_company.objects.get(id=request.POST.get("sel_company"))
        tbl_model.objects.create(model_name=name,company=comid)
        return redirect("Admin:Model")

    return render(request,'Adminstrator/Model.html',{'companydata':companydata,'modeldata':modeldata})



def BodyType(request):
    if 'aid' not in request.session:
        return redirect('Guest:Login')
    body_data=tbl_body.objects.all()
    if request.method=="POST":
        body=request.POST.get("txt_body")
        tbl_body.objects.create(
            body_name=body
        )
        return redirect("Admin:BodyType")
    else:
        return render(request,'Adminstrator/BodyType.html',{'body':body_data}) 

def DoorCount(request):
    if 'aid' not in request.session:
        return redirect('Guest:Login')
    door_data=tbl_door.objects.all()
    if request.method=="POST":
        door_value=request.POST.get("txt_door")
        tbl_door.objects.create(
            door_value=door_value
        )
        return redirect("Admin:DoorCount")
    else:
        return render(request,'Adminstrator/DoorCount.html',{'door':door_data})   

def SeatingCapacity(request):
    if 'aid' not in request.session:
        return redirect('Guest:Login')
    seat_data=tbl_seat.objects.all()
    if request.method=="POST":
        seat_value=request.POST.get("txt_seat")
        tbl_seat.objects.create(
            seat_value=seat_value
        )
        return redirect("Admin:SeatingCapacity")
    else:
        return render(request,'Adminstrator/SeatingCapacity.html',{'seat':seat_data})    

def FuelType(request):
    if 'aid' not in request.session:
        return redirect('Guest:Login')
    fuel_data=tbl_fuel.objects.all()
    if request.method=="POST":
        fuel_value=request.POST.get("txt_fuel")
        tbl_fuel.objects.create(
            fuel_value=fuel_value
        )
        return redirect("Admin:FuelType")
    else:
        return render(request,'Adminstrator/FuelType.html',{'fuel':fuel_data})  

def EngineConfiguration(request):
    if 'aid' not in request.session:
        return redirect('Guest:Login')
    engine_data=tbl_engine.objects.all()
    if request.method=="POST":
        engine_value=request.POST.get("txt_engine")
        tbl_engine.objects.create(
            engine_value=engine_value
        )
        return redirect("Admin:EngineConfiguration")
    else:
        return render(request,'Adminstrator/EngineConfiguration.html',{'engine':engine_data})

def TransmissionType(request):
    if 'aid' not in request.session:
        return redirect('Guest:Login')
    transmission_data=tbl_transmission.objects.all()
    if request.method=="POST":
        transmission_value=request.POST.get("txt_transmission")
        tbl_transmission.objects.create(
            transmission_value=transmission_value
        )
        return redirect("Admin:TransmissionType")
    else:
        return render(request,'Adminstrator/TransmissionType.html',{'transmission':transmission_data})

def OwnershipCount(request):
    if 'aid' not in request.session:
        return redirect('Guest:Login')
    ownershipcount_data=tbl_ownershipcount.objects.all()
    if request.method=="POST":
        ownershipcount_type=request.POST.get("txt_ownershipcount")
        tbl_ownershipcount.objects.create(
            ownershipcount_type=ownershipcount_type
        )
        return redirect("Admin:OwnershipCount")
    else:
        return render(request,'Adminstrator/OwnershipCount.html',{'ownershipcount':ownershipcount_data})

def DriveTrain(request):
    if 'aid' not in request.session:
        return redirect('Guest:Login')
    drivetrain_data=tbl_drivetrain.objects.all()
    if request.method=="POST":
        drivetrain_type=request.POST.get("txt_drivetrain")
        tbl_drivetrain.objects.create(
           drivetrain_type=drivetrain_type
        )
        return redirect("Admin:DriveTrain")
    else:
        return render(request,'Adminstrator/DriveTrain.html',{'drivetrain':drivetrain_data})

def companydelete(request,id):
    tbl_company.objects.get(id=id).delete()
    return redirect("Admin:Company")


def modeldelete(request,id):
    tbl_model.objects.get(id=id).delete()
    return redirect("Admin:Model")
    


def bodydelete(request,id):
    tbl_body.objects.get(id=id).delete()
    return redirect("Admin:BodyType")

def doordelete(request,id):
    tbl_door.objects.get(id=id).delete()
    return redirect("Admin:DoorCount")

def seatdelete(request,id):
    tbl_seat.objects.get(id=id).delete()
    return redirect("Admin:SeatingCapacity")

def fueldelete(request,id):
    tbl_fuel.objects.get(id=id).delete()
    return redirect("Admin:FuelType")

def enginedelete(request,id):
    tbl_engine.objects.get(id=id).delete()
    return redirect("Admin:EngineConfiguration")

def transmissiondelete(request,id):
    tbl_transmission.objects.get(id=id).delete()
    return redirect("Admin:TransmissionType")

def drivetraindelete(request,id):
    tbl_drivetrain.objects.get(id=id).delete()
    return redirect("Admin:DriveTrain")

def ownershipcountdelete(request,id):
    tbl_ownershipcount.objects.get(id=id).delete()
    return redirect("Admin:OwnershipCount")



def deletedistrict(request,id):
    tbl_district.objects.get(id=id).delete()
    return redirect("Admin:District")


def deletecategory(request,id):
    tbl_category.objects.get(id=id).delete()
    return redirect("Admin:Category")

def deleteadminregistration(request,id):
    tbl_adminregistration.objects.get(id=id).delete()
    return redirect("Admin:AdminRegistration")

def deletebrand(request,id):
    tbl_brand.objects.get(id=id).delete()
    return redirect("Admin:Brand")

def deletetype(request,id):
    tbl_type.objects.get(id=id).delete()
    return redirect("Admin:Type")

def deletesubcategory(request,id):
    tbl_subcategory.objects.get(id=id).delete()
    return redirect("Admin:SubCategory")

def editdistrict(request,id):
    district=tbl_district.objects.get(id=id)
    if request.method=="POST":
        districtdata=request.POST.get("txt_district")
        district.district_name=districtdata
        district.save()
        return redirect("Admin:District")
    return render(request,'Adminstrator/District.html',{'editdata':district})

def companyedit(request,id):
    company=tbl_company.objects.get(id=id)
    if request.method=="POST":
        company_data=request.POST.get("txt_company")
        company.company_name=company_data
        company.save()
        return redirect("Admin:Company")
    return render(request,'Adminstrator/Company.html',{'editdata':company})

def bodyedit(request,id):
    body=tbl_body.objects.get(id=id)
    if request.method=="POST":
        body_data=request.POST.get("txt_body")
        body.body_name=body_data
        body.save()
        return redirect("Admin:BodyType")
    return render(request,'Adminstrator/BodyType.html',{'editdata':body})

def dooredit(request,id):
    door=tbl_door.objects.get(id=id)
    if request.method=="POST":
        door_data=request.POST.get("txt_door")
        door.door_value=door_data
        door.save()
        return redirect("Admin:DoorCount")
    return render(request,'Adminstrator/DoorCount.html',{'editdata':door})

def seatedit(request,id):
    seat=tbl_seat.objects.get(id=id)
    if request.method=="POST":
        seat_data=request.POST.get("txt_seat")
        seat.seat_value=seat_data
        seat.save()
        return redirect("Admin:SeatingCapacity")
    return render(request,'Adminstrator/SeatingCapacity.html',{'editdata':seat})


def fueledit(request,id):
    fuel=tbl_fuel.objects.get(id=id)
    if request.method=="POST":
        fuel_data=request.POST.get("txt_fuel")
        fuel.fuel_value=fuel_data
        fuel.save()
        return redirect("Admin:FuelType")
    return render(request,'Adminstrator/FuelType.html',{'editdata':fuel})

def engineedit(request,id):
    engine=tbl_engine.objects.get(id=id)
    if request.method=="POST":
        engine_data=request.POST.get("txt_engine")
        engine.engine_value=engine_data
        engine.save()
        return redirect("Admin:EngineConfiguration")
    return render(request,'Adminstrator/EngineConfiguration.html',{'editdata':engine})

def transmissionedit(request,id):
    transmission=tbl_transmission.objects.get(id=id)
    if request.method=="POST":
        transmission_data=request.POST.get("txt_transmission")
        transmission.transmission_value=transmission_data
        transmission.save()
        return redirect("Admin:TransmissionType")
    return render(request,'Adminstrator/TransmissionType.html',{'editdata':transmission})

def drivetrainedit(request,id):
    drivetrain=tbl_drivetrain.objects.get(id=id)
    if request.method=="POST":
        drivetrain_data=request.POST.get("txt_drivetrain")
        drivetrain.drivetrain_type=drivetrain_data
        drivetrain.save()
        return redirect("Admin:DriveTrain")
    return render(request,'Adminstrator/DriveTrain.html',{'editdata':drivetrain})

def ownershipcountedit(request,id):
    ownershipcount=tbl_ownershipcount.objects.get(id=id)
    if request.method=="POST":
        ownershipcount_data=request.POST.get("txt_ownershipcount")
        ownershipcount.ownershipcount_type=ownershipcount_data
        ownershipcount.save()
        return redirect("Admin:OwnershipCount")
    return render(request,'Adminstrator/OwnershipCount.html',{'editdata':ownershipcount})



def modeledit(request,id):
    model=tbl_model.objects.get(id=id)
    company_data=tbl_company.objects.all()

    if request.method=="POST":
        model_data=request.POST.get("txt_model")
        model.model_name=model_data
        model.save()
        return redirect("Admin:Model")
    return render(request,'Adminstrator/Model.html',{'editdata':model,'companydata':company_data})



def editcategory(request,id):
    category=tbl_category.objects.get(id=id)
    if request.method=="POST":
        categorydata=request.POST.get("txt_category")
        category.category_name=categorydata
        category.save()
        return redirect("Admin:Category")
    return render(request,'Adminstrator/Category.html',{'editdata':category})

def editadminregistration(request,id):
    adminregistration=tbl_adminregistration.objects.get(id=id)
    if request.method=="POST":
        namedata=request.POST.get("txt_name")
        contactdata=request.POST.get("txt_contact")
        emaildata=request.POST.get("txt_email")
        passworddata=request.POST.get("txt_password")
        adminregistration.adminregistration_name=namedata
        adminregistration.adminregistration_contact=contactdata
        adminregistration.adminregistration_email=emaildata
        adminregistration.adminregistration_password=passworddata
        adminregistration.save()
        return redirect("Admin:AdminRegistration")
    return render(request,'Adminstrator/AdminRegistration.html',{'editdata':adminregistration})

def editbrand(request,id):
    brand=tbl_brand.objects.get(id=id)
    if request.method=="POST":
        branddata=request.POST.get("txt_brand")
        brand.brand_name=branddata
        brand.save()
        return redirect("Admin:Brand")
    return render(request,'Adminstrator/Brand.html',{'editdata':brand})

def edittype(request,id):
    ty=tbl_type.objects.get(id=id)
    if request.method=="POST":
        typedata=request.POST.get("txt_type")
        ty.type_name=typedata
        ty.save()
        return redirect("Admin:Type")
    return render(request,'Adminstrator/Type.html',{'editdata':ty})

def editsubcategory(request,id):
    category=tbl_category.objects.all()
    subcategory=tbl_subcategory.objects.get(id=id)
    if request.method=="POST":
        subcategoryoption=tbl_category.objects.get(id=request.POST.get("sel_category"))
        subcategorydata=request.POST.get("txt_subcategory")
        subcategory.category=subcategoryoption
        subcategory.sub_name=subcategorydata
        subcategory.save()
        return redirect("Admin:SubCategory")
    return render(request,'Adminstrator/SubCategory.html',{'editdata':subcategory,"categorydata":category})

def useraccept(request,uid):
    accdata=tbl_user.objects.get(id=uid)
    accdata.user_status = 1
    accdata.save()
    return render(request,'Adminstrator/UserList.html',{'msg':'accept'})

def userreject(request,uid):
    rejdata=tbl_user.objects.get(id=uid)
    rejdata.user_status = 2
    rejdata.save()
    return render(request,'Adminstrator/UserList.html',{'msg':'reject'})

def dealeraccept(request,did):
    accdata=tbl_dealer.objects.get(id=did)
    accdata.dealer_status = 1
    accdata.save()
    return render(request,'Adminstrator/DealerList.html',{'msg':'accept'})

def dealerreject(request,did):
    rejdata=tbl_dealer.objects.get(id=did)
    rejdata.dealer_status = 2
    rejdata.save()
    return render(request,'Adminstrator/DealerList.html',{'msg':'reject'})

def YearCount(request):
    if 'aid' not in request.session:
        return redirect('Guest:Login')
    year_data=tbl_year.objects.all()
    if request.method=="POST":
        year_value=request.POST.get("txt_year")
        tbl_year.objects.create(
            year_value=year_value
        )
        return redirect("Admin:YearCount")
    else:
        return render(request,'Adminstrator/ModelYear.html',{'year':year_data})  

def yeardelete(request,id):
    tbl_year.objects.get(id=id).delete()
    return redirect("Admin:YearCount")

def yearedit(request,id):
    year=tbl_year.objects.get(id=id)
    if request.method=="POST":
        year_data=request.POST.get("txt_year")
        year.year_value=year_data
        year.save()
        return redirect("Admin:YearCount")
    return render(request,'Adminstrator/ModelYear.html',{'editdata':year})

def Logout(request):
    if 'aid' not in request.session:
        return redirect('Guest:Login')
    del request.session['aid']
    return redirect('Guest:Login')