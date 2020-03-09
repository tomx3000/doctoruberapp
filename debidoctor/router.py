from rest_framework import routers
from doctorapp.api.viewsets import UserViewSet,RoleDataViewSet,SpecializationViewSet,UserRelationshipViewSet,DiseaseViewSet,SymptomViewSet,MedicalProfileViewSet,LocationViewSet,FilesAttachedViewSet

router = routers.DefaultRouter()

router.register("user",UserViewSet ,basename='user')
router.register("role",RoleDataViewSet)
router.register("specialization",SpecializationViewSet)
router.register("userrelation",UserRelationshipViewSet)
router.register("disease",DiseaseViewSet)
router.register("symptom",SymptomViewSet)
router.register("medicalprofile",MedicalProfileViewSet)
router.register("location",LocationViewSet)
router.register("attachments",FilesAttachedViewSet)

