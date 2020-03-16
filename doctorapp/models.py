from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


# Create your models here.

class Role(models.Model):
	role_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=255,null=True,blank=True,verbose_name="role name")
	description = models.CharField(max_length=255,null=True,blank=True)
	updated_at=models.DateTimeField(auto_now=True,null=True,blank=True)
	created_at=models.DateTimeField(auto_now_add=True,null=True,blank=True)

	def __str__(self):
		return(str(self.role_id)+": "+ self.name)

	class Meta:
		db_table = "role"

# note extending the abstractuser forces us to create this user table at the veyb begning , before anytable is in the db., this is done so as to avoid some heavy configurations to make django admin panel work 

# so remember that next time you are trying to tranfer the db to another server
class User(AbstractUser):
    # note usename is the phoenuber
	phone = models.CharField(max_length=15,blank=True,null=True)
	gender = models.CharField(max_length=15,null=True,blank=True)
	role_id= models.ForeignKey(Role,on_delete=models.CASCADE,blank=True,null=True)
	user_type = models.CharField(max_length=60,null=True,blank=True)
	date_of_birth=models.DateField(null=True,blank=True)
	updated_at=models.DateTimeField(auto_now=True,null=True,blank=True)
	created_at=models.DateTimeField(auto_now_add=True,null=True,blank=True)
	users = models.ManyToManyField('self', through='UserRelationship',symmetrical=False)
	medical_profile = models.ManyToManyField("MedicalProfile",blank=True)
	location = models.ManyToManyField("Location",blank=True)
	specialization = models.ManyToManyField("Specialization",blank=True)
	profile_image = models.FileField(upload_to="image_%y_%m_%d",null=True,blank=True)
	otp = models.CharField(max_length=15,blank=True,null=True)
	def __str__(self):
		return str(self.id)+":"+str(self.username)

	class Meta:
		db_table = "users"
  
      
class UserRelationship(models.Model):
    # types = models.ManyToManyField('RelationshipType', blank=True,
	# 								related_name='user_relationships')
    doctor = models.ForeignKey('User', related_name='doctors',on_delete=models.CASCADE)
    patient = models.ForeignKey('User', related_name='patients',on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ('doctor', 'patient')


class Specialization(models.Model):
    name = models.CharField(max_length=60,null=True,blank=True)
    disease = models.ManyToManyField("Disease",blank=True)
    updated_at=models.DateTimeField(auto_now=True,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    
    def __str__(self):
        return str(self.name)
        pass

class Disease(models.Model):
    name = models.CharField(max_length=60,null=True,blank=True)
    updated_at=models.DateTimeField(auto_now=True,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    symptom = models.ManyToManyField("Symptom")
    
    def __str__(self):
        return str(self.name)
        pass

class Symptom(models.Model):
	name = models.CharField(max_length=60,null=True,blank=True)
	updated_at=models.DateTimeField(auto_now=True,null=True,blank=True)
	created_at=models.DateTimeField(auto_now_add=True,null=True,blank=True)
	
	def __str__(self):
		return str(self.name)
		
     
class MedicalProfile(models.Model):
    symptom = models.ManyToManyField(Symptom)
    weight = models.FloatField(default=0,blank=True,null=True)
    height = models.FloatField(default=0,blank=True,null=True)
    age = models.IntegerField(default=0,blank=True,null=True)
    body_temperatue = models.FloatField(default=0,blank=True,null=True)
    body_pressure = models.CharField(max_length=15,blank=True,null=True)
    infection_image =models.FileField(upload_to="image_%y_%m_%d",null=True,blank=True)
    updated_at=models.DateTimeField(auto_now=True,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    
    def __str__(self):
        return str(self.id)

class FilesAttached(models.Model):
    name = models.CharField(max_length=15,blank=True,null=True)
    profile = models.ForeignKey('MedicalProfile', related_name='doctors',on_delete=models.CASCADE)
    infection_image =models.FileField(upload_to="attachment_%y_%m_%d",null=True,blank=True)
    
    def __str__(self):
        return self.name
        
    
class Location(models.Model):
    longitude = models.CharField(max_length=60,null=True,blank=True)
    latitude = models.CharField(max_length=60,null=True,blank=True)
    country = models.CharField(max_length=60,null=True,blank=True)
    region = models.CharField(max_length=60,null=True,blank=True)
    city = models.CharField(max_length=60,null=True,blank=True)
    district = models.CharField(max_length=60,null=True,blank=True)
    street = models.CharField(max_length=60,null=True,blank=True)
    
    
    def __str__(self):
        return str(country)
    
