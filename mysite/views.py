from rest_framework.viewsets import ModelViewSet
# from rest_framework_swagger.views import get_swagger_view
# from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from .serializers import *
from .models import *
from . import query_params
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.parsers import FormParser, MultiPartParser

# schema_view = get_swagger_view(title='Pastebin API')




class MahsulotlarViewSet(ModelViewSet):
    queryset = Mahsulotlar.objects.all()
    serializer_class = MahsulotlarSerializers