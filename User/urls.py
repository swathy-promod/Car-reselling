from django.urls import path
from User import views
app_name='User'
urlpatterns=[

    path('HomePage/',views.HomePage,name='HomePage'),
    path('MyProfile/',views.MyProfile,name='MyProfile'),
    path('EditProfile/',views.EditProfile,name='EditProfile'),
    path('ChangePassword/',views.ChangePassword,name='ChangePassword'),
    path('Complaint/',views.Complaint,name='Complaint'),
    path('Feedback/',views.Feedback,name='Feedback'), 
    path('Viewvehicle/',views.Viewvehicle,name="Viewvehicle"),
    path("Viewvehicle/", views.Viewvehicle, name="Viewvehicle"),
    path("BookVehicle/<int:id>/", views.BookVehicle, name="BookVehicle"),
    path("MyBooking/", views.MyBooking, name="MyBooking"),
    path('rating/<int:mid>',views.rating,name="rating"),  
    path('ajaxstar/',views.ajaxstar,name="ajaxstar"),
    path('starrating/',views.starrating,name="starrating"),
    path("payment/<int:vid>",views.payment,name="payment"),
    path('loader/',views.loader, name='loader'),
    path('paymentsuc/',views.paymentsuc, name='paymentsuc'),
    path("logout/",views.logout,name="logout"),
    path('PricePrediction/',views.predict_car_price,name="PricePrediction"),
    path('Logout/',views.Logout,name="Logout"),

]

