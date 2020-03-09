from django.shortcuts import render,get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.decorators import login_required
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate,login,logout
from django.core import serializers
from rest_framework.permissions import AllowAny,IsAuthenticated
from .forms import ImageForm
from .models import User,Role,UserRelationship,Specialization,Disease,Symptom,MedicalProfile,Location
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
# Create your views here.

from .sms import SMS
@csrf_exempt
@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def AddProfile(request,*args,**kargs):
    token = Token.objects.filter(key=request.META.get('HTTP_AUTHORIZATION').strip()[5:].strip())
    
    if len(token)>0:        
        form = ImageForm(request.POST,request.FILES,instance=token[0].user)
        if form.is_valid():
            photo = form.save()
        SMS(password="1234",phonenumber="0684905873").send(phonenumber="0767236526",message="123456")
        return Response({"success":True}, status=HTTP_200_OK)
    return Response({"success":False}, status=HTTP_400_BAD_REQUEST)
    
 

