from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse
from django.http import JsonResponse
from feed.models import Students
# Create your views here.
def index(request):
    return render(request,"index.html")
def second_page(request):
    name=(request.POST.get("rollNumber"))
    password=(request.POST.get("password"))
    data={'message':"success"}
    return JsonResponse(data)
def second_pages(request):
    save = Students.objects.filter(reg="20cse050").values('reg', 'deptid',"name","yearid")
    
    reg=(save[0]['reg'])       # Access the 'reg' field for the first student
    dept=(save[0]['deptid'])
    year=save[0]["yearid"]
    if(int(dept)==1 ):
        dept="CSE"
    else:
        dept="IT"    # Access the 'deptid' field for the first student
    name=(save[0]['name'])
    context = {
            'reg': reg,
            'dept': dept,
            'name': name,
            'year':year
        }
    return render(request,"second.html",context)