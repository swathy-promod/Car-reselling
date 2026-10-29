from django.shortcuts import render,redirect
from Adminstrator.models import *
from User.models import *
from Dealer.models import tbl_vehicle
from Guest.models import tbl_user
from decimal import Decimal
from django.http import JsonResponse
import pickle
from datetime import datetime
import pandas as pd




def HomePage(request):
    if 'uid' not in request.session:
        return redirect('Guest:Login')
    userdata=tbl_user.objects.get(id=request.session['uid'])
    return render(request,'User/HomePage.html',{'user':userdata})



def MyProfile(request):
    if 'uid' not in request.session:
        return redirect('Guest:Login')
    userdata=tbl_user.objects.get(id=request.session['uid'])

    return render(request,'User/MyProfile.html',{'user':userdata})

def EditProfile(request):
    if 'uid' not in request.session:
        return redirect('Guest:Login')
    userdata=tbl_user.objects.get(id=request.session['uid'])
    if request.method=="POST":
        userdata.user_name=request.POST.get("txt_name")
        userdata.user_email=request.POST.get("txt_email")
        userdata.user_contact=request.POST.get("txt_contact")
        userdata.user_address=request.POST.get("txt_address")
        userdata.save()
        return render(request,"User/Myprofile.html",{'msg':"profile updated"})
   
    return render(request,'User/EditProfile.html',{'user':userdata})

def ChangePassword(request):
    if 'uid' not in request.session:
        return redirect('Guest:Login')
    user=tbl_user.objects.get(id=request.session['uid'])
   
    if request.method=='POST':
        oldpassword=request.POST.get("txt_oldpsw")
        newpassword=request.POST.get("txt_newpsw")
        retypepassword=request.POST.get("txt_retypepsw")

        if user.user_password==oldpassword:
            if newpassword==retypepassword:
                user.user_password=newpassword
                user.save()
                return render(request,"User/MyProfile.html",{"msg":"password change successfully"})
            else:
                return render(request,"User/ChangePassword.html",{"msg":"new password do not mach"})
        else:
            return render(request,'User/ChangePassword.html',{"msg":"old password incorrect"})
    else:
        return render(request,"User/ChangePassword.html")

def Complaint(request):
    if 'uid' not in request.session:
        return redirect('Guest:Login')
    complaint=tbl_complaint.objects.all()
    user=tbl_user.objects.get(id=request.session['uid'])
    if request.method=='POST':
        title=request.POST.get("txt_title")
        content=request.POST.get("txt_content")
        tbl_complaint.objects.create(
            complaint_title=title,
            complaint_content=content,
            user=user
        )
        return redirect("User:Complaint")
    return render(request,'User/Complaint.html',{'complaint':complaint})

def Feedback(request):
    if 'uid' not in request.session:
        return redirect('Guest:Login')
    feedback=tbl_feedback.objects.all()
    user=tbl_user.objects.get(id=request.session['uid'])
    if request.method == 'POST':
        content=request.POST.get("txt_content")
        tbl_feedback.objects.create(
            feedback_content=content,
            user=user
        )
        return redirect("User:Feedback")
    return render(request,'User/Feedback.html',{'feedback':feedback})
    

def Viewvehicle(request):
    if 'uid' not in request.session:
        return redirect('Guest:Login')
    Viewvehicle_data = tbl_vehicle.objects.all()
    return render(request, 'User/Viewvehicle.html', {'Viewvehicle': Viewvehicle_data})




# def Viewvehicle(request):
#     addvehicle = tbl_vehicle.objects.all()
#     return render(request, "User/Viewvehicle.html", {"addvehicle": addvehicle})

def BookVehicle(request, id):
    if 'uid' not in request.session:
        return redirect('Guest:Login')
    current_vehicle = tbl_vehicle.objects.get(id=id)  
    amount = current_vehicle.vehicle_price
    tbl_booking.objects.create(
        vehicle=current_vehicle,
        user=tbl_user.objects.get(id=request.session['uid']),
        booking_amount = amount
    )
    return redirect("User:MyBooking")




def MyBooking(request):
    if 'uid' not in request.session:
        return redirect('Guest:Login')
    uid=request.session['uid']
    booking_data = tbl_booking.objects.filter(user=request.session['uid'])

    return render(request, "User/MyBooking.html", {"bookings": booking_data})

def payment(request,vid):
    if 'uid' not in request.session:
        return redirect('Guest:Login')
    booking=tbl_booking.objects.get(id=vid)
    vehicle= booking.vehicle.vehicle_price
    amount = vehicle*.10
    counts = tbl_booking.objects.filter(id=vid,user_id=request.session["uid"],booking_status=3).count()
    print(counts)
    if counts > 0:
        return render(request,"User/Payment.html",{"msg":"Payment Already Done.."})
    else:
        if request.method == "POST":
            booking.booking_status=3
            booking.booking_amount = amount
            booking.save()
            return redirect("User:loader")
        else:
            return render(request,"User/Payment.html",{'amount':amount})

def loader(request):
    if 'uid' not in request.session:
        return redirect('Guest:Login')
    return render(request,"User/Loader.html")

def paymentsuc(request):
    if 'uid' not in request.session:
        return redirect('Guest:Login')
    return render(request,"User/Payment_suc.html")



def rating(request,mid):
    if 'uid' not in request.session:
        return redirect('Guest:Login')
    parray=[1,2,3,4,5]
    mid=mid
    # wdata=tbl_booking.objects.get(id=mid)
    
    counts=0
    counts=stardata=tbl_rating.objects.filter(dealer=mid).count()
    if counts>0:
        res=0
        stardata=tbl_rating.objects.filter(dealer=mid).order_by('-datetime')
        for i in stardata:
            res=res+i.rating_data
        avg=res//counts
        # print(avg)
        return render(request,"User/Rating.html",{'mid':mid,'data':stardata,'ar':parray,'avg':avg,'count':counts})
    else:
         return render(request,"User/Rating.html",{'mid':mid})

def ajaxstar(request):
    parray=[1,2,3,4,5]
    rating_data=request.GET.get('rating_data')
    
    user_review=request.GET.get('user_review')
    pid=request.GET.get('pid')
    # wdata=tbl_booking.objects.get(id=pid)
    tbl_rating.objects.create(user=tbl_user.objects.get(id=request.session['uid']),user_review=user_review,rating_data=rating_data,dealer=tbl_dealer.objects.get(id=pid))
    stardata=tbl_rating.objects.filter(dealer=pid).order_by('-datetime')
    return render(request,"User/AjaxRating.html",{'data':stardata,'ar':parray})

def starrating(request):
    if 'uid' not in request.session:
        return redirect('Guest:Login')
    r_len = 0
    five = four = three = two = one = 0
    # cdata = tbl_booking.objects.get(id=request.GET.get("pdt"))
    rate = tbl_rating.objects.filter(dealer=request.GET.get("pdt"))
    ratecount = tbl_rating.objects.filter(dealer=request.GET.get("pdt")).count()
    for i in rate:
        if int(i.rating_data) == 5:
            five = five + 1
        elif int(i.rating_data) == 4:
            four = four + 1
        elif int(i.rating_data) == 3:
            three = three + 1
        elif int(i.rating_data) == 2:
            two = two + 1
        elif int(i.rating_data) == 1:
            one = one + 1
        else:
            five = four = three = two = one = 0
        # print(i.rating_data)
        # r_len = r_len + int(i.rating_data)
    # rlen = r_len // 5
    # print(rlen)
    result = {"five":five,"four":four,"three":three,"two":two,"one":one,"total_review":ratecount}
    return JsonResponse(result)

def logout(request):
    if 'uid' not in request.session:
        return redirect('Guest:Login')
    del request.session['uid']
    return redirect('Guest:Index')




model = pickle.load(open("Assets/Model/car_price_model.pkl","rb"))

brand_encoder = pickle.load(open("Assets/Model/brand_encoder.pkl","rb"))
model_encoder = pickle.load(open("Assets/Model/model_encoder.pkl","rb"))
trans_encoder = pickle.load(open("Assets/Model/trans_encoder.pkl","rb"))
owner_encoder = pickle.load(open("Assets/Model/owner_encoder.pkl","rb"))
fuel_encoder = pickle.load(open("Assets/Model/fuel_encoder.pkl","rb"))

def predict_car_price(request):
    if 'uid' not in request.session:
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

    return render(request,"User/PricePrediction.html",{"price":price,'companydata':companydata,'Modelyear':modelyeardata})

def Logout(request):
    if 'uid' not in request.session:
        return redirect('Guest:Login')
    del request.session['uid']
    return redirect('Guest:Login')