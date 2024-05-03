from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import certificate_form
# Create your views here.

def home(request):
    if request.method=="POST":
        form_id=request.POST['id']
        form_name=request.POST['name']
        form_email=request.POST['email']
        form_course=request.POST['course']
        form_trainer=request.POST['trainer']
        form_phone=request.POST['phone']

        obj=certificate_form()
        obj.reg_no=form_id
        obj.name=form_name
        obj.email=form_email
        obj.course=form_course
        obj.trainer=form_trainer
        obj.phone=form_phone
        obj.save()

        my_certificate_form=certificate_form.objects.all()

        return render(request, 'read.html', {'datas': my_certificate_form})
    
    return render(request, 'home.html')

def read(request):
    my_certificate_form=certificate_form.objects.all()

    return render(request, 'read.html', {'datas': my_certificate_form})

def update(request,id):
    update=certificate_form.objects.get(id=id)
    if request.method=="POST":
        form_id=request.POST['id']
        form_name=request.POST['name']
        form_email=request.POST['email']
        form_course=request.POST['course']
        form_trainer=request.POST['trainer']
        form_phone=request.POST['phone']
    
        update.reg_no=form_id
        update.name=form_name
        update.email=form_email
        update.course=form_course
        update.trainer=form_trainer
        update.phone=form_phone
        update.save()
        
        return redirect('read')
        
    return render(request,'update.html', {'data':update})

def delete_form(request,id):
    delete_data=certificate_form.objects.get(id=id)
    delete_data.delete()
    return redirect('read')