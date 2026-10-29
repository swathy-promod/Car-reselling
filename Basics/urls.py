from django.urls import path
from Basics import views
app_name='Basics'
urlpatterns = [
    path('Sum/',views.Sum,name="Sum"),
    path('Calculator/',views.Calculator,name="Calculator"),
    path('Largest/',views.Largest,name="Largest"),
    path('Three/',views.LargestThree,name="LargestThree"),
    path('RankList/',views.RankList,name="RankList"),
    path('SalaryCalculation/',views.SalaryCalculation,name="SalaryCalculation"),
]