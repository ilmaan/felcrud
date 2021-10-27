from django.forms.widgets import PasswordInput
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render, HttpResponsePermanentRedirect
# import requests
import io

from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
# import requests
from rest_framework.parsers import JSONParser
from .models import Library
from .serializers import LibrarySerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse

from .forms import Book_Registration

from django.contrib.auth.models import User, auth



# Create your views here.
@csrf_exempt
def Library_api(request):
    if request.method == 'GET':
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

    if request.method == 'POST':
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


    if request.method == 'PUT':
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


    if request.method == 'DELETE':
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
