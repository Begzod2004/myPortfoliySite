from rest_framework import serializers
from .models import *


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = "__all__"
    

class MyResumeSerializer(serializers.ModelSerializer):

    class Meta:
        model = MyResume
        fields = "__all__"



class MyProjectsSerializer(serializers.ModelSerializer):

    class Meta:
        model = MyProjects
        fields = "__all__"


class MySkillsSerializer(serializers.ModelSerializer):

    class Meta:
        model = MySkills
        fields = "__all__"


class MyWorkExpreaSerializer(serializers.ModelSerializer):

    class Meta:
        model = MyWorkExprea
        fields = "__all__"


class GetInTouchSerializer(serializers.ModelSerializer):

    class Meta:
        model = GetInTouch
        fields = "__all__"