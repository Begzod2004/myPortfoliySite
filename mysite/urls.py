from django.db import router
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.routers import SimpleRouter
from rest_framework_swagger.views import get_swagger_view
from django.conf import settings
from django.conf.urls.static import static
from .views import *
router = DefaultRouter()


router = SimpleRouter()
router.register('Comment', CommentViewSet)
router.register('MyResume', MyResumeViewSet)
router.register('MyprojectsViewSet', MyprojectsViewSet)
router.register('MySkills', MySkillsViewSet)
router.register('MyWorkExprea', MyWorkExpreaViewSet)
router.register('GetInTouch', GetInTouchViewSet)




urlpatterns = [ 
    path("", include(router.urls)),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

