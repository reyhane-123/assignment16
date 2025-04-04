from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Users,Course
from django.db.models import Q
def list(request):
    s=Users(name="hana",family="askari",phone="09338121166",email="hana@gmail.com",password="321")      
    s.save()
    
    return HttpResponse('hi')

def filterr(request):
    c=Course.objects.exclude(Q(is_deleted=True)|Q(is_deleted=1)|Q(is_deleted=2)|Q(is_deleted=3))
    return render(request,'app/list.html',{'list':c})


def update(request,id):
    a=Users.get(id=id)
    n=request.GET.get('name','')
    a.name=n
    a.save()

def detail(request,id):
    d=Course.get(id=id)
    return render(request,'app/detail.html',{'detaill':d})