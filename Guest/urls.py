from django.urls import path
from Guest import views
app_name='Guest'
urlpatterns = [
    path('NewUser/',views.NewUser,name='NewUser'),
    path('ajaxplace/',views.ajaxplace,name='ajaxplace'),
    path('Login/',views.Login,name='Login'),
    path('VehicledealerRegistration/',views.VehicledealerRegistration,name='VehicledealerRegistration'),
    path('',views.Index,name='Index'),
    path('forgotpassword/',views.forgotpassword,name="forgotpassword"),
    path('otp/',views.otp,name="otp"),
    path('newpass/',views.newpass,name="newpass"),
]
