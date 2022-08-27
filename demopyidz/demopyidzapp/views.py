from django.http import HttpResponse
from django.shortcuts import render
from .models import place
from .models import team
from .models import main

# Create your views here.
def demo(request):
  objx=place.objects.all()
  objy=team.objects.all()
  objz=main.objects.all()
  return  render(request,"index.html",{'result':objx, 'resultb':objy, 'resulta':objz,})






# def addition(request):
#   x=int (request.GET['num1'])
#   y=int (request.GET['num2'])
#   res=x+y
#   res1=x-y
#   res2=x*y
#   res3=x/y
#   return  render(request,"result.html",{'result':res,'sub':res1,'multi':res2,'divi':res3})
#def contact(request):
 # return HttpResponse("www.uefa.com")
#def details(request):
 # return render(request,"details.html")
#def thanks(request):
 # return HttpResponse("Thanks")