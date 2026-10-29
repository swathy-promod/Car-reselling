from django.urls import path
from Dealer import views
app_name='Dealer'
urlpatterns=[

    path('HomePage/',views.HomePage,name='HomePage'),
    path('MyProfile/',views.MyProfile,name='MyProfile'),
    path('EditProfile/',views.EditProfile,name='EditProfile'),
    path('ChangePassword/',views.ChangePassword,name='ChangePassword'), 
    path('AddVehicle/',views.AddVehicle,name='AddVehicle'),
    path('ajaxmodel/',views.ajaxmodel,name='ajaxmodel'),
    path('vehicledelete/<int:id>/',views.vehicledelete,name="vehicledelete"),
    path('Myvehicle/', views.Myvehicle, name='Myvehicle'),
    path('Gallery/<int:id>', views.Gallery, name='Gallery'),
    path('Gallerydelete/<int:id>/', views.gallerydelete, name='Gallerydelete'),
    path('ViewBooking/', views.ViewBooking, name='ViewBooking'),
    path('acceptbooking/<int:bid>/',views.bookingaccept,name="acceptbooking"),
    path('rejectbooking/<int:bid>/',views.bookingreject,name="rejectbooking"),
    path('PricePrediction/',views.predict_car_price,name="PricePrediction"),
    path('Logout/',views.Logout,name="Logout"),
]
