from rest_framework.viewsets import ModelViewSet
# from rest_framework_swagger.views import get_swagger_view
# from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.parsers import FormParser, MultiPartParser

# schema_view = get_swagger_view(title='Pastebin API')




class CommentViewSet(ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer


class MyResumeViewSet(ModelViewSet):
    queryset = MyResume.objects.all()
    serializer_class = MyResumeSerializer

    
class MyprojectsViewSet(ModelViewSet):
    queryset = MyProjects.objects.all()
    serializer_class = MyProjectsSerializer

    

class MySkillsViewSet(ModelViewSet):
    queryset = MySkills.objects.all()
    serializer_class = MySkillsSerializer

    


class MyWorkExpreaViewSet(ModelViewSet):
    queryset = MyWorkExprea.objects.all()
    serializer_class = MyWorkExpreaSerializer

    


class GetInTouchViewSet(ModelViewSet):
    queryset = GetInTouch.objects.all()
    serializer_class = GetInTouchSerializer

    

