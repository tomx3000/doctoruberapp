from django.contrib import admin
from .models import User,Role,UserRelationship,Specialization,Disease,Symptom,MedicalProfile,Location,FilesAttached
# Register your models here.

admin.site.register(User)
admin.site.register(Role)
admin.site.register(UserRelationship)
admin.site.register(Specialization)
admin.site.register(Disease)
admin.site.register(Symptom)
admin.site.register(MedicalProfile)
admin.site.register(Location)
admin.site.register(FilesAttached)

