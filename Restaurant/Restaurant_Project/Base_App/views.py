from django.shortcuts import render
from django.http import HttpResponse
from Base_App.models import BookTable, Items, ItemList, AboutUs,Feedback


# Create your views here.
def HomeView(request):
    items = Items.objects.all()
    list = ItemList.objects.all()
  
    return render(request,'home.html')

def AboutView(request):
        
      return render(request, 'about.html')


def MenuView(request):
    items = Items.objects.all()
    list = ItemList.objects.all()

    #content = {'items':items}
   
   # return render (request,'menu.html',content)
    return render (request,'menu.html',{'items' : items, 'list' : list})





def BookTableView(request):
      if request.method=='POST':
            name = request.POST.get('user_name')
            phone_number = request.POST.get('phone_number')
            email = request.POST.get('user_email')
            total_person = request.POST.get('total_person')
            booking_data = request.POST.get('booking_data')

            if name !='' and len (phone_number) == 10 and email != '' and total_person != 0 and booking_data != '':
                data = BookTable(Name=name, Phone_number=phone_number,
                                 Email=email,Total_person=total_person,
                                 Booking_date=booking_data)
            
                data.save()

      return render(request,'book_table.html')



def FeedbackView(request):
      return HttpResponse('Hi,this is my feedback page')
