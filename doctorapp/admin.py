from django.contrib import admin
from .models import User,Role,UserRelationship,Specialization,Disease,Symptom,MedicalProfile,Location,FilesAttached
# Register your models here.
admin.site.site_header = "LIFE SAVING NETWORK"
admin.site.site_title ="LIFE SAVING NETWORK"
admin.site.index_title = "Life saving network administration"

admin.site.register(User)
admin.site.register(Role)
admin.site.register(UserRelationship)
admin.site.register(Specialization)
admin.site.register(Disease)
admin.site.register(Symptom)
admin.site.register(MedicalProfile)
admin.site.register(Location)
admin.site.register(FilesAttached)

