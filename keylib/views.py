from django.forms.widgets import PasswordInput
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render, HttpResponsePermanentRedirect
# import requests
import io

from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
# import requests
from rest_framework.parsers import JSONParser
from .models import Employee, Library, Hero
from .serializers import EmployeeSerializer, LibrarySerializer, HeroSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from .forms import Book_Registration

from django.contrib.auth.models import User, auth

from django.utils.decorators import method_decorator
from django.views import View

from rest_framework import viewsets
from rest_framework.response import Response


# Create your views here.

# ##################### CLASS BASED VIEW ############

class employee_api_class(APIView):
    def get(self, request,pk=None, format=None):
        # id = request.data.get('id')
        id = pk
        if id is not None:
            emp = Employee.objects.get(id=id)
            serializer = EmployeeSerializer(emp)
            return Response(serializer.data)

        emp = Employee.objects.all()
        serializer = EmployeeSerializer(emp, many=True)
        return Response(serializer.data)

    def post(self,request,pk=None, format=None):
        data = request.data
        serializer = EmployeeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Added'})
        return Response(serializer.errors) 


    def put(self,request,pk=None, format=None):
        # id = request.data.get('id')
        id = pk
        emp = Employee.objects.get(pk=id)
        data = request.data
        serializer = EmployeeSerializer(emp,data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Put Data Updated'})
        return Response(serializer.errors)

    
    def patch(self,request,pk=None, format=None):
        # id = request.data.get('id')
        id = pk
        emp = Employee.objects.get(pk=id)
        data = request.data
        serializer = EmployeeSerializer(emp,data=data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Patch Data Updated'})
        return Response(serializer.errors)


    def delete(self,request,pk=None, format=None):
        # id = request.data.get('id')
        id = pk
        emp = Employee.objects.get(pk=id)
        emp.delete()
        return Response({'msg':'Data Deleeted'}) 



################CRUD REST ###############

@api_view(['GET','POST','PUT','DELETE','PATCH'])
def employee_api(request,pk=None):
    if request.method == 'GET':
        # id = request.data.get('id')
        id = pk
        if id is not None:
            emp = Employee.objects.get(id=id)
            serializer = EmployeeSerializer(emp)
            return Response(serializer.data)

        emp = Employee.objects.all()
        serializer = EmployeeSerializer(emp, many=True)
        return Response(serializer.data)

    if request.method =='POST':
        data = request.data
        serializer = EmployeeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Added'})
        return Response(serializer.errors)    

    if request.method == 'PUT':
        # id = request.data.get('id')
        id = pk
        emp = Employee.objects.get(pk=id)
        data = request.data
        serializer = EmployeeSerializer(emp,data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Updated'})
        return Response(serializer.errors)

    
    if request.method == 'PATCH':
        # id = request.data.get('id')
        id = pk
        emp = Employee.objects.get(pk=id)
        data = request.data
        serializer = EmployeeSerializer(emp,data=data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Updated'})
        return Response(serializer.errors)


    if request.method == 'DELETE':
        # id = request.data.get('id')
        id = pk
        emp = Employee.objects.get(pk=id)
        emp.delete()
        return Response({'msg':'Data Deleeted'})    




################CRUD REST ###############







# MEDIUM _STACK OVERFLOW CRUD

class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer


#################################

# @api_view()
# def func1(request):
#     return Response({'msg':'Cradence'})


# @api_view(['POST'])
# def func1(request):
#     if request.method == 'POST':
#         print(request.data)
#         return Response({'msg':'Bradence'})


@api_view(['GET','POST'])
def func1(request):
    if request.method == 'GET':
        print(request.data)
        return Response({'msg':'GET REQUEST'})

    if request.method == 'POST':
        print(request.data)
        return Response({'msg':'POST REQUEST'})




#########################################






# Class Based view 

@method_decorator(csrf_exempt, name='dispatch')
class Library_api(View):
    def get(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id',None)
        if id is not None:
            lib = Library.objects.get(id=id)
            serializer =  LibrarySerializer(lib)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='application/json')

        lib = Library.objects.all()
        serializer = LibrarySerializer(lib, many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='application/json')

    def post(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = LibrarySerializer(data = python_data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Book Added'}
            # json_data = JSONRenderer().render(res)
            # return HttpResponse(json_data,content_type='application/json') 
            return JsonResponse(res)

        
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')

    def put(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        lib = Library.objects.get(id=id)
        serializer = LibrarySerializer(lib, data= python_data,partial=True)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Book Updated'}
            # json_data = JSONRenderer().render(res)
            # return HttpResponse(json_data, content_type='application/json')
            return JsonResponse(res)
        
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')

    def delete(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        lib = Library.objects.get(id=id)
        lib.delete()
        res = {'msg':'Data Deleted'}
        # json_data= JSONRenderer().render(res)
        # return HttpResponse(json_data, content_type='application/json')
        return JsonResponse(res,safe=False)



# Function Based View

# @csrf_exempt
# def Library_api(request):
#     if request.method == 'GET':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         python_data = JSONParser().parse(stream)
#         id = python_data.get('id',None)
#         if id is not None:
#             lib = Library.objects.get(id=id)
#             serializer =  LibrarySerializer(lib)
#             json_data = JSONRenderer().render(serializer.data)
#             return HttpResponse(json_data, content_type='application/json')

#         lib = Library.objects.all()
#         serializer = LibrarySerializer(lib, many=True)
#         json_data = JSONRenderer().render(serializer.data)
#         return HttpResponse(json_data, content_type='application/json')

#     if request.method == 'POST':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         python_data = JSONParser().parse(stream)
#         serializer = LibrarySerializer(data = python_data)
#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg':'Book Added'}
#             # json_data = JSONRenderer().render(res)
#             # return HttpResponse(json_data,content_type='application/json') 
#             return JsonResponse(res)

        
#         json_data = JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data,content_type='application/json') 


#     if request.method == 'PUT':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         python_data = JSONParser().parse(stream)
#         id = python_data.get('id')
#         lib = Library.objects.get(id=id)
#         serializer = LibrarySerializer(lib, data= python_data,partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg':'Book Updated'}
#             # json_data = JSONRenderer().render(res)
#             # return HttpResponse(json_data, content_type='application/json')
#             return JsonResponse(res)
        
#         json_data = JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data, content_type='application/json')


#     if request.method == 'DELETE':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         python_data = JSONParser().parse(stream)
#         id = python_data.get('id')
#         lib = Library.objects.get(id=id)
#         lib.delete()
#         res = {'msg':'Data Deleted'}
#         # json_data= JSONRenderer().render(res)
#         # return HttpResponse(json_data, content_type='application/json')
#         return JsonResponse(res,safe=False)





def addshow(request):
    if request.method == 'POST':
        fm = Book_Registration(request.POST)
        if fm.is_valid():
            
            bn = fm.cleaned_data['bname']
            ba = fm.cleaned_data['bauthor']
            bq = fm.cleaned_data['bquantity']
            reg = Library(bname=bn,bauthor=ba,bquantity=bq)

            reg.save()
            fm = Book_Registration()
    else:
        fm = Book_Registration()
        
    lib = Library.objects.all()
        

    return render(request,'manage.html',{'form':fm,'lib':lib})


  
def deletebook(request,id):
    if request.method == 'POST':
        li = Library.objects.get(pk=id)
        li.delete()
        return HttpResponseRedirect('/')




def updatebook(request,id):
    if request.method == 'POST':
        li = Library.objects.get(pk=id)
        fm = Book_Registration(request.POST,instance=li)
        if fm.is_valid():
            fm.save()

    else:
        li = Library.objects.get(pk=id)
        fm = Book_Registration(instance=li)
        


    return render(request,'update.html',{'form':fm})



def index(request):
    return render(request,'index.html')


def allbooks(request):
    lib = Library.objects.all()
        

    return render(request,'allbooks.html',{'lib':lib})


def login(request):
    if request.method == 'POST':
        username = request.POST['Username']
        password = request.POST['Password'] 

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('addshow')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')




    else:
        return render(request,'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        if password==cpassword:
            if User.objects.filter(username=username).exists():
                print("username taken")
                messages.info(request,"Username taken")
                return redirect('register')
                
            elif User.objects.filter(email=email).exists():
                print("email taken")
                messages.info(request,"Email taken")
                return redirect('register')

            else:    
                user = User.objects.create_user(username=username,email=email,password=password)
                user.save()
                return redirect('login')
        else:
            print("Password do not match")


        return redirect('/')

    else:
        return render(request,'register.html')