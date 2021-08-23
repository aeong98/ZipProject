from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.shortcuts import render, get_list_or_404

from .models import Curation,CurationComment,CurationTag
from .serializers import CurationSerializer,CurationCommentSerializer,CurationTagSerializer

class CurationViewSet(viewsets.ModelViewSet):
    queryset = Curation.objects.all()
    serializer_class = CurationSerializer

class CurationCommentViewSet(viewsets.ModelViewSet):
    queryset = CurationComment.objects.all()
    serializer_class = CurationCommentSerializer

class CurationTagViewSet(viewsets.ModelViewSet):
    queryset = CurationTag.objects.all()
    serializer_class = CurationTagSerializer

curation_list = CurationViewSet.as_view({'get': 'list'})
comment_list = CurationCommentViewSet.as_view({'get': 'list'})
tag_list = CurationTagViewSet.as_view({'get': 'list'})