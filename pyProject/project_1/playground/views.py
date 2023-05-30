from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#request -> respoonse
#request handler
#action

def sayHello (request) : 
   return render(request,'hello.html', {'name': 'Julian'})
