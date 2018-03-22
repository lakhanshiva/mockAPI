# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.renderers import StaticHTMLRenderer
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, viewsets
from django.http import HttpResponse
from django.template import Context, loader
import requests

# Create your views here.
from django.contrib.auth.models import User, Group
from mockAPI.quickstart.models import Project, UserDetails
from rest_framework import viewsets
from mockAPI.quickstart.serializers import UserSerializer, GroupSerializer, ProjectSerializer, UserDetailsSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class UserDetailsViewSet(APIView):
    queryset = UserDetails.objects.all()
    serializer_class = UserDetailsSerializer
    def get(self, request, *args, **kwargs):
        url = 'https://jsonplaceholder.typicode.com/posts'
        r = requests.get(url)
        data = r.json()
        data_list = {'data': data}
        return Response(data_list)
