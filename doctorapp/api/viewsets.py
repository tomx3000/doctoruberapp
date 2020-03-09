from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import UserSerializer,RoleSerializer,UserRelationshipSerializer,SpecializationSerializer,DiseaseSerializer,SymptomSerializer,MedicalProfileSerializer,LocationSerializer,FilesAttachedSerializer
from doctorapp.models import User,Role,UserRelationship,Specialization,Disease,Symptom,MedicalProfile,Location,FilesAttached
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from doctorapp.sms import SMS
import random
class UserLoginAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)

        if not created:  
        	token.delete()
        	token = Token.objects.create(user=user)
        return Response({
            'token': token.key,
            'success':True 
        })
    

# class UserViewSet(viewsets.ModelViewSet):
# 	queryset = User.objects.all()
# 	serializer_class = UserSerializer
# 	# permission_classes=(AllowAny,)

class UserViewSet(viewsets.ViewSet):
    def get_permissions(self):
        
        if self.action == 'create':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
        
    def create(self, request):
        print(request.data)
        user, created_user = User.objects.get_or_create(username=request.data["username"])
        user.set_password(request.data.get("password","1234"))
        user.first_name=request.data.get("first_name","")
        user.last_name=request.data.get("last_name","")
        user.user_type=request.data.get("user_type","patient")
        user.gender=request.data.get("gender","female")
        otp = random.randint(999,10000)
        user.otp=otp
        user.save()
        token, created = Token.objects.get_or_create(user=user)
        
        if not created:  
        	token.delete()
        	token = Token.objects.create(user=user)
        SMS(password="1234",phonenumber="0684905873").send(phonenumber=request.data.get("username","0767236526"),message="Life Saving Network, otp "+str(otp))
        return Response({"token":token.key,"id":user.id,"phonenumber":user.username,"first_name":user.first_name,"last_name":user.last_name,"gender":user.gender,"user_type":user.user_type,"otp":user.otp})
        
    
    def list(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
    # @action(methods=['post'],detail=False)
	# def updateprofileimage(self,request,*args,**kwargs):
	# 	user=User.objects.get(id=int(kwargs['userid']))
  
 


    def update(self, request, pk=None):
        pass
    

class RoleDataViewSet(viewsets.ModelViewSet):
	queryset = Role.objects.all()
	serializer_class = RoleSerializer
	# permission_classes=(AllowAny,)
 
 
class SpecializationViewSet(viewsets.ModelViewSet):
	queryset = Specialization.objects.all()
	serializer_class = SpecializationSerializer
	# permission_classes=(AllowAny,)


class UserRelationshipViewSet(viewsets.ModelViewSet):
	queryset = UserRelationship.objects.all()
	serializer_class = UserRelationshipSerializer
	# permission_classes=(AllowAny,)

 
class DiseaseViewSet(viewsets.ModelViewSet):
	queryset = Disease.objects.all()
	serializer_class = DiseaseSerializer
	# permission_classes=(AllowAny,)


class SymptomViewSet(viewsets.ModelViewSet):
	queryset = Symptom.objects.all()
	serializer_class = SymptomSerializer
	# permission_classes=(AllowAny,)
 
 
class MedicalProfileViewSet(viewsets.ModelViewSet):
	queryset = MedicalProfile.objects.all()
	serializer_class = MedicalProfileSerializer
	# permission_classes=(AllowAny,)


class LocationViewSet(viewsets.ModelViewSet):
	queryset = Location.objects.all()
	serializer_class = LocationSerializer
	# permission_classes=(AllowAny,)
 
 
 
class FilesAttachedViewSet(viewsets.ModelViewSet):
	queryset = FilesAttached.objects.all()
	serializer_class = FilesAttachedSerializer
	# permission_classes=(AllowAny,)
 
 
 