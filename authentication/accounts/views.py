from django.shortcuts import render
from rest_framework.decorators import list_route, detail_route
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET', 'POST'])
@csrf_exempt
@list_route(methods = ['POST'])
def login(request):
    response={}
    email=request.data['email_id']
    password=request.data['password']

    # check if email d and password exists in DB
    user=authenticate(username=email,password=password)

    #if user exits
    if user is not None :
        return Response("Wow! loggedin")
        #return Response(status=status.HTTP_201_CREATED)
    elif User.objects.filter(email=email).exists():
        return Response("Invalid Credentials!")
    else:
        return Response("Email id not registered! Please regitester this email id")


@api_view(['GET', 'POST'])
@csrf_exempt
@list_route(methods = ['POST'])
def create(request):
    print("in the functn")
    response={}
    first_name=request.data['first_name']
    last_name=request.data['last_name']
    email=request.data['email_id']
    password=request.data['password']

    if User.objects.filter(email=email).exists():
        response['message']="email id already registered"
        return Response(response)

    #create new user
    else:
        new_user=User.objects.create_user(username=email,email=email,password=password,first_name=first_name,last_name=last_name)
        new_user.save()
        return Response("account created!")

@api_view(['GET', 'POST'])
@csrf_exempt
@list_route(methods = ['POST'])
def reset(request):
    response={}
    email=request.data['email_id']
    new_password=request.data['new_password']

    #check if email id is in DB
    if User.objects.filter(email=email).exists():
        user=User.objects.get(email=email)
        user.set_password(new_password)
        user.save()
        response['message']="Resest password successful"
        return Response(response)
    else:
        response['message']="Email id not found"
        return Response(response)




