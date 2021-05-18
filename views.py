from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpRequest
from . models import User,Apartments,complaint_section

# Create your views here.



def home(request):
    return render(request,'OurProject/home.html')








def insert_complaint_section_info(request):
    if request.method == 'POST':
        complaint_section_Info=complaint_section(user_id=request.POST.get('User'),title=request.POST.get('Title'),description=request.POST.get('Description'),home_address=request.POST.get('HomeAddress'),police_station=request.POST.get('PoliceStation'))
        complaint_section_Info.save()
        return HttpResponse("Your complaint has been recieved")
    else:
       return render(request,'OurProject/complaint_section.html')
def insert_user_info(request):
  #  AppartmentId=User(request.GET['apartment_id'])
    UserInfo=User(first_name=request.POST.get('FirstName'),last_name=request.POST.get('LastName'),phone_number=request.POST.get('PhoneNumber'),user_type=request.POST.get('UserType'))
    UserInfo.save()
    
    return HttpResponse("Congratulations!You are successfully registered to Nagorik Seba")


   
def insert_Apartment_info(request):
     if request.method == 'POST':
       ApartmentInfo=Apartments(flat_number=request.POST.get('FlatNumber'),building_name=request.POST.get('BuildingName'),building_number=request.POST.get('BuildingNumber'),building_address=request.POST.get('BuildingAddress'),flat_size=request.POST.get('FlatSize'),num_of_beds=request.POST.get('NumOfBeds'),num_of_toilet=request.POST.get('NumOfToilet'),num_of_balcony=request.POST.get('NumOfBalcony'),map_address=request.POST.get('MapAddress'),location=request.POST.get('Location'))
       ApartmentInfo.save()
       return HttpResponse("Your Apartment Profile is updated")
     else:
       return render(request,'OurProject/apartment.html')



   
   