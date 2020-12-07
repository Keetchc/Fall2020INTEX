from django.shortcuts import render
from django.http import request, HttpResponse

# Create your views here.

def indexPageView(request) :
   return render(request, 'homepages/index.html')

def aboutPageView(request) :
    sOutput = '<html><head><title>My Title</title></head><body><p style="color:red;"><b>one</b></p><p style="color:blue;">two</p><p style="font-size:50px;">three</p><ul><li>A</li><li>B</li><li>C</li></ul></body></html>'
    return HttpResponse(sOutput)
    