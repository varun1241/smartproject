from django.shortcuts import render,redirect,HttpResponseRedirect,reverse
from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm,authenticate,UserChangeForm,PasswordChangeForm
from .forms import RegistrationForm,EditForm
from django.contrib.auth import login
from django import forms
from django.contrib.auth import logout as django_logout
from django.contrib.auth.decorators import login_required
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Studentfrom,Employee
from .serializers import StudentSerializer
#from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,authenticate

def register(request):

    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'login.html')
        else:
            return render(request,'register.html',{'form':form})
    else:
        form = RegistrationForm()
        return render(request,'register.html',{'form':form})
  
def login_process(request):
    if request.method =="POST":
        username= request.POST.get("username")
        password= request.POST.get("password")
        user = authenticate(username=username,password=password)#if none then the data stored is none
        if user:
            login(request,user)
            return render(request,'home.html')
        else:
            return render(request,'login.html',{"error": True})

    
    return render(request,'login.html')

def logout_process(request):
    django_logout(request)
    return render(request,'out.html')

def delete_user(self):
    self.User.delete()
    return render(request,'login.html')






def edit(request):

    if request.method == "POST":
        form = EditForm(request.POST,instance=request.user)#to indentify the user and make changes
        if form.is_valid():
            form.save()
            return redirect(home)
        else:
            return render(request,'register.html',{'form':form})
    else:
        form = EditForm(instance=request.user)
        return render(request,'edit.html',{'form':form})

def passowrdchange(request):

    if request.method == "POST":
        form = PasswordChangeForm(data=request.POST,user=request.user)#to indentify the user and make changes
        if form.is_valid():
            form.save()
            return render(request,'login.html')
        else:
            return render(request,'change.html',{'form':form})
    else:
        form = PasswordChangeForm(user=request.user)
        return render(request,'change.html',{'form':form})


@login_required(login_url='/login/')

def home(request):

    return render(request,'home.html')

def user(request):
    

    student2=Studentfrom.objects.all()
    return render(request,'user.html',{'student2':student2})#directory is created in that contains all details of student


class StudentList(APIView):

    

    def get(self, request):
        stuendts1=Studentfrom.objects.all()
        serializer=StudentSerializer(stuendts1,many=True)
        return Response(serializer.data)

    def post(self,request):
        sterlizeobj=StudentSerializer(data=request.data)
        if sterlizeobj.is_valid():
            sterlizeobj.save()
            return Response(sterlizeobj.data,status=status.HTTP_201_CREATED)
        else:
            return Response(sterlizeobj.errors,status=status.HTTP_400_BAD_REQUEST)

class Studentupdate(APIView):
    
    def get_object(self,pk):

        try:
            return Studentfrom.objects.get(pk=pk)
        
        except Studentfrom.DoesNotExist:
            return Response(sterlizeobj.errors,status=status.HTTP_400_BAD_REQUEST)
    def get(self,request,pk):

        emobj=self.get_object(pk)
        sterlizeobj=StudentSerializer(emobj)
        return Response(sterlizeobj.data)
    
    def put(self,request,pk):

        emobj=self.get_object(pk)
        stustelize=StudentSerializer(emobj,data=request.data)

        if stustelize.is_valid():
            stustelize.save()
            return Response(stustelize.data,status=status.HTTP_201_CREATED)
        else:
            return Response(stustelize.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):

        emobj=self.get_object(pk)
        emobj.delete()
        return Response(status=status.HTTP_200_OK)



def add(request):
   if request.method == "POST":
      Employe_name=request.POST.get("Employe_name")
      Employe_phone=request.POST.get("Employe_phone")
      Employe_department=request.POST.get("Employe_department")
      Employe_Email=request.POST.get("Employe_Email")
      Employe_Adress=request.POST.get("Employe_Adress")
      uploaded_file = request.FILES['document']
      #fs = FileSystemStorage()
      #name = fs.save(uploaded_file.name,uploaded_file)
      #url = fs.url(name)
      obj=Employee(name=Employe_name, phone=Employe_phone, department=Employe_department ,email=Employe_Email, picture=uploaded_file,address=Employe_Adress)
      obj.save()

      return redirect("home")
      
   
   #code
   else:
      
      return render(request,'add.html')
def show(request):
    employee=Employee.objects.all()
    context={
            "employee":employee
            }
    return render(request,'show.html',context)

