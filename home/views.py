from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
   # return HttpResponse("hello")
   peoples=[
       {"name":"Avantika","age":34},
       {"name":"Rajat","age":14},
       {"name":"Shakuntala","age":64},

   ]
   text="hey i am a certified web developer"
   return render(request,"home\index.html",context={"peoples":peoples,"text":text})
def contact(request):
    return render(request,"home\contact.html")
def about(request):
    return render(request,"home/about.html")
def success_page(request):
    return HttpResponse("<h1>hey,this is a success page<h1>")
