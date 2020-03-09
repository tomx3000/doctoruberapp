from rest_framework import serializers
from doctorapp.models import User,Role,UserRelationship,Specialization,Disease,Symptom,MedicalProfile,Location,FilesAttached



class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields ="__all__"


class RoleSerializer(serializers.ModelSerializer):
	class Meta:
		model = Role
		fields ="__all__"


class UserRelationshipSerializer(serializers.ModelSerializer):
	class Meta:
		model = UserRelationship
		fields ="__all__"


class SpecializationSerializer(serializers.ModelSerializer):
	class Meta:
		model = Specialization
		fields ="__all__"

class DiseaseSerializer(serializers.ModelSerializer):
	class Meta:
		model = Disease
		fields ="__all__"


class SymptomSerializer(serializers.ModelSerializer):
	class Meta:
		model = Symptom
		fields ="__all__"

class MedicalProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model = MedicalProfile
		fields ="__all__"


class LocationSerializer(serializers.ModelSerializer):
	class Meta:
		model = Location
		fields ="__all__"


class FilesAttachedSerializer(serializers.ModelSerializer):
	class Meta:
		model = FilesAttached
		fields ="__all__"  

