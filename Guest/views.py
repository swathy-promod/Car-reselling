from django.shortcuts import render,redirect
from Guest.models import *
from Adminstrator.models import *
import random
from django.core.mail import send_mail
from django.conf import settings

def NewUser(request):
    newuser_data=tbl_user.objects.all()
    district=tbl_district.objects.all() 
    place_data=tbl_place.objects.all()
    if request.method=="POST":
        name=request.POST.get("txt_name")
        gender=request.POST.get("rd_gender")
        contact=request.POST.get("txt_contact")
        email=request.POST.get("txt_email")
        password=request.POST.get("txt_psw")
        address=request.POST.get("txt_address")
        photo=request.FILES.get("file_photo")
        proof=request.FILES.get("file_proof")
        placeid=tbl_place.objects.get(id=request.POST.get("sel_place"))
       
        tbl_user.objects.create(
            user_name=name,
            user_gender=gender,
            user_contact=contact,
            user_email=email,
            user_password=password,
            user_address=address,
            user_photo=photo,
            user_proof=proof,
            place=placeid
        )
        return redirect("Guest:NewUser")
    return render(request,'Guest/NewUser.html',{'user':newuser_data,'place':place_data,'district':district})    

def ajaxplace(request):
    did=request.GET.get("did")
    place=tbl_place.objects.filter(district=did)
    return render(request, 'Guest/Ajaxplace.html',{'place':place})       
     
def Login(request):
    if request.method=="POST":
        email=request.POST.get("txt_email")
        password=request.POST.get("txt_password")
        admincount=tbl_adminregistration.objects.filter(adminregistration_email=email,adminregistration_password=password).count()
        usercount= user=tbl_user.objects.filter(user_email=email,user_password=password).count()
        dealercount=tbl_dealer.objects.filter(dealer_email=email,dealer_password=password).count()
        if admincount>0:
            admin=tbl_adminregistration.objects.get(adminregistration_email=email,adminregistration_password=password)
            request.session['aid']=admin.id
            return redirect("Admin:HomePage")
        elif  usercount>0:
            user=tbl_user.objects.get(user_email=email,user_password=password)
            if user.user_status==0:
                return render(request,'Guest/Login.html',{'msg':"Registration is pending"})
            elif user.user_status==2:
                return render(request,'Guest/Login.html',{'msg':"Registration is Rejected"})
            else:
                request.session['uid']=user.id
                return redirect("User:HomePage")
        elif dealercount>0:
                dealer=tbl_dealer.objects.get(dealer_email=email,dealer_password=password)
                if dealer.dealer_status == 0:
                    return render(request,"Guest/Login.html",{'msg':"Registration is pending"})
                elif dealer.dealer_status == 2:
                    return render(request,"Guest/Login.html",{'msg':"Registration is rejected"})
                else: 
                    request.session['did']=dealer.id
                    return redirect("Dealer:HomePage")
        else:
            return render(request,'Guest/Login.html')
    
    return render(request,'Guest/Login.html')



def VehicledealerRegistration(request):
    VehicledealerRegistration_data=tbl_user.objects.all()
    district=tbl_district.objects.all() 
    place_data=tbl_place.objects.all()
    if request.method=="POST":
        name=request.POST.get("txt_name")
        contact=request.POST.get("txt_contact")
        email=request.POST.get("txt_email")
        password=request.POST.get("txt_psw")
        address=request.POST.get("txt_address")
        date=request.POST.get("txt_date")
        oname=request.POST.get("txt_oname")
        ocontact=request.POST.get("txt_ocontact")
        photo=request.FILES.get("file_photo")
        oproof=request.FILES.get("file_photo")
        photo=request.FILES.get("file_photo")
        proof=request.FILES.get("file_proof")
        logo=request.FILES.get("file_logo")
        placeid=tbl_place.objects.get(id=request.POST.get("sel_place"))
        tbl_dealer.objects.create(
            dealer_name=name,
            dealer_contact=contact,
            dealer_email=email,
            dealer_password=password,
            dealer_address=address,
            established_date=date,
            owner_name=oname,
            owner_contact=ocontact,
            owner_photo=photo,
            owner_proof=oproof,
            licence_proof=proof,            
            dealer_place=placeid,
            dealer_logo=logo
        )
        return redirect("Guest:VehicledealerRegistration")
    return render(request,'Guest/VehicledealerRegistration.html',{'dealer':VehicledealerRegistration_data,'place':place_data,'district':district})



def Index(request):
    
    return render(request, 'Guest/Index.html') 



def forgotpassword(request):
    if request.method == "POST":
        email = request.POST.get("txt_email")
        usercount = tbl_user.objects.filter(user_email=email).count()
        if usercount>0:
            user = tbl_user.objects.get(user_email=email)
            otp = random.randint(111111,999999)
            request.session["otp"] = otp
            request.session["fid"] = user.id
            send_mail(
                'Forgot password OTP', #subject
                "\rHello \r" + str(otp) +"\n This is the OTP to reset ur password.\n If you didn't ask to reset your password, you can ignore this email. \r\n Thanks. \r\n Your D MARKET team.",#body
                settings.EMAIL_HOST_USER,
                [email],
            )
            return render(request,"Guest/ForgotPassword.html",{"msg":email})
        else:
            return render(request,"Guest/ForgotPassword.html",{"msg":"Account Doesnt Exist.."})

    else:
        return render(request,"Guest/ForgotPassword.html")

def otp(request):
    if request.method == "POST":
        inp_otp = int(request.POST.get("txt_otp"))
        if inp_otp == request.session["otp"]:
            return redirect("Guest:newpass")
        else:
            return render(request,"Guest/OTP.html",{"msg":"OTP Does not Matches..!!"})
    else:
        return render(request,"Guest/OTP.html")

def newpass(request):
    if request.method == "POST":
        user = tbl_user.objects.get(id=request.session["fid"])
        if request.POST.get("txt_new_pass") == request.POST.get("txt_con_pass"):
            user.user_password = request.POST.get("txt_con_pass")
            user.save()
            return render(request,"Guest/NewPassword.html",{"msg1":"Password Updated Sucessfully...."})
        else:
            return render(request,"Guest/NewPassword.html",{"msg":"Error in confirm password..!!!"})
    else:
        return render(request,"Guest/NewPassword.html")