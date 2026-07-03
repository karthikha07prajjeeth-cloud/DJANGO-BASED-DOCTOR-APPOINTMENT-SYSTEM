from django.shortcuts import render
from app.models import *
# Create your views here.
def index_page(request):
    return render(request,'index.html')
def about_page(request):
    return render(request,'about.html')
def doctor_page(request):
    data = doctor.objects.all()
    a = data.count()
    print(a)
    return render(request,'doctor.html',{'data':data})
def product_detail(request,id):
    d=doctor.objects.get(id=id)
    return render(request, 'product_detail.html',{'d':d})
def success_page(request):
    return render(request, 'success.html')